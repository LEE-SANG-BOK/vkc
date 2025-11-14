"""
FastMCP 서버 스켈레톤 (로컬 파일 search/fetch)

설치:
  pip install fastmcp

실행(HTTP):
  fastmcp run vkc-agents/mcp/server.py:mcp --transport http --port 8000

도구:
  - search(query): canon/gpts/ops/prompts 등 텍스트 파일에서 질의어 검색
  - fetch(id): id(파일 경로)를 받아 전문 반환

주의: PDF는 기본적으로 무시(텍스트 추출 미구현). 필요시 OCR/텍스트 추출 추가.
"""

from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, List

from fastmcp import FastMCP

ROOT = Path(__file__).resolve().parents[1]
SEARCH_DIRS = [
    ROOT / "canon",
    ROOT / "gpts",
    ROOT / "ops",
    ROOT / "prompts",
    ROOT / "funnel",
    ROOT / "content",
    ROOT / "brand",
    ROOT / "knowledge",
]

PDF_SUFFIXES = {".pdf"}
TEXT_SUFFIXES = {".md", ".txt", ".json"}

mcp = FastMCP("VKC-MCP")


def _collect_files() -> List[Path]:
    files: List[Path] = []
    for d in SEARCH_DIRS:
        if d.exists():
            for p in d.rglob("*"):
                if p.is_file() and (p.suffix.lower() in TEXT_SUFFIXES or p.suffix.lower() in PDF_SUFFIXES):
                    files.append(p)
    return files


def _read_pdf_text(path: Path) -> str:
    try:
        # Optional dependency: PyPDF2
        import PyPDF2  # type: ignore
        text_parts: List[str] = []
        with path.open("rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages[:25]:  # cap pages for speed
                try:
                    text_parts.append(page.extract_text() or "")
                except Exception:
                    continue
        return "\n".join(text_parts)
    except Exception:
        return ""  # gracefully degrade if not available


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def search(query: str) -> Dict:
    """검색 도구. 쿼리에 매칭되는 로컬 파일 스니펫을 반환(PDF 일부 포함).

    Returns JSON: {"results": [{"id", "title", "url", "content"}, ...]}
    """
    q = query.strip().lower()
    results = []
    for p in _collect_files():
        text = ""
        if p.suffix.lower() in TEXT_SUFFIXES:
            text = _read_text(p)
        elif p.suffix.lower() in PDF_SUFFIXES:
            text = _read_pdf_text(p)
        if not text:
            continue
        if q in text.lower():
            snippet = text[:1000]
            results.append({
                "id": str(p),
                "title": p.name,
                "url": f"file://{p}",
                "content": snippet,
            })
        if len(results) >= 10:
            break
    return {"results": results}


def fetch(id: str) -> Dict:
    """가져오기 도구. id(파일 경로)를 받아 전문 일부(최대 50k) 반환.

    Returns JSON: {"id", "title", "url", "content"}
    """
    p = Path(id)
    if not p.exists() or not p.is_file():
        return {"error": f"not found: {id}"}
    text = ""
    if p.suffix.lower() in PDF_SUFFIXES:
        text = _read_pdf_text(p)
    else:
        text = _read_text(p)
    # trim overly long
    if len(text) > 50000:
        text = text[:50000]
    return {
        "id": str(p),
        "title": p.name,
        "url": f"file://{p}",
        "content": text,
    }


if __name__ == "__main__":
    # 툴 등록 후 stdio 실행 지원 (개발용)
    try:
        mcp.tool(search)
        mcp.tool(fetch)
    except Exception:
        pass
    mcp.run()
