"""Simple MCP bridge to execute remote tools via the Model Context Protocol.

This module connects to an MCP server that exposes tools (search/fetch, etc.)
over the Streamable HTTP transport. It converts tool call requests from the
Assistants API into MCP `call_tool` invocations and serializes the responses so
they can be submitted back as tool outputs.
"""

from __future__ import annotations

import asyncio
import json
from dataclasses import dataclass
from typing import Any, Dict

from mcp import ClientSession, types
from mcp.client.streamable_http import streamablehttp_client


class MCPBridgeError(RuntimeError):
    """Raised when the MCP bridge cannot execute a tool."""


@dataclass(frozen=True)
class BridgeTool:
    """Represents a mapping between an Assistants API tool and an MCP tool."""

    assistant_name: str
    mcp_name: str


class MCPBridge:
    """Executes mapped MCP tools and returns serialized outputs."""

    def __init__(self, server_url: str, tool_map: Dict[str, BridgeTool]):
        self.server_url = server_url.rstrip("/")
        self.tool_map = tool_map

    def available_tools(self) -> Dict[str, BridgeTool]:
        return self.tool_map

    def execute(self, tool_name: str, arguments: Dict[str, Any]) -> str:
        if tool_name not in self.tool_map:
            raise MCPBridgeError(f"Unknown MCP tool: {tool_name}")
        bridge_tool = self.tool_map[tool_name]
        return asyncio.run(self._call_remote(bridge_tool.mcp_name, arguments or {}))

    async def _call_remote(self, remote_tool_name: str, arguments: Dict[str, Any]) -> str:
        async with streamablehttp_client(self.server_url) as (read, write, _):
            async with ClientSession(read, write) as session:
                await session.initialize()
                result = await session.call_tool(remote_tool_name, arguments)
                return self._serialize_result(result)

    @staticmethod
    def _serialize_result(result: types.CallToolResult) -> str:
        structured = getattr(result, "structuredContent", None)
        if structured is not None:
            return json.dumps(structured, ensure_ascii=False)

        texts = []
        for content in getattr(result, "content", []) or []:
            text_value = getattr(content, "text", None)
            if text_value:
                texts.append(text_value)
                continue
            resource = getattr(content, "resource", None)
            if resource is None:
                continue
            resource_text = getattr(resource, "text", None)
            if resource_text:
                texts.append(resource_text)
                continue
            if hasattr(resource, "data") and resource.data:
                texts.append(str(resource.data))

        if texts:
            return "\n".join(texts)

        if getattr(result, "isError", False):
            return json.dumps({"error": "MCP tool execution failed."}, ensure_ascii=False)

        return json.dumps({"status": "ok"}, ensure_ascii=False)
