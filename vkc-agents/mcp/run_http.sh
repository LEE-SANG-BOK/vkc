#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/.."

echo "[MCP] Creating/activating venv at .venv (optional)…"
if [ ! -d .venv ]; then
  python3 -m venv .venv || true
fi
if [ -f .venv/bin/activate ]; then
  source .venv/bin/activate
fi

echo "[MCP] Installing requirements (fastmcp, PyPDF2)…"
pip install -q -r mcp/requirements.txt || pip install fastmcp PyPDF2 || true

echo "[MCP] Starting HTTP server on :8000"
exec fastmcp run mcp/server.py:mcp --transport http --port 8000
