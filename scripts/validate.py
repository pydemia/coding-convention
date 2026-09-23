"""Validate dictionary files without importing example dependencies."""

from __future__ import annotations

import ast
import re
import sys
import tomllib
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit


def markdown_anchors(text: str) -> set[str]:
    """Collect explicit anchors and the simple headings used in this bundle."""
    anchors = set(re.findall(r'<a id="([^"]+)"', text))
    for heading in re.findall(r"^#{1,6} (.+)$", text, re.MULTILINE):
        slug = re.sub(r"[^\w\s-]", "", heading).lower().replace(" ", "-")
        anchors.add(slug)
    return anchors


def markdown_links(text: str) -> list[str]:
    """Find inline and reference links in the maintained Markdown subset."""
    inline = re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", text)
    references = re.findall(r"^\[[^\]]+\]:\s+(\S+)", text, re.MULTILINE)
    return inline + references


def check_markdown(path: Path, text: str, root: Path) -> list[str]:
    """Check link targets, anchors, fenced Python syntax, and prose width."""
    root = root.resolve()
    path = path.resolve()
    errors: list[str] = []
    relative = path.relative_to(root)
    fence: str | None = None
    block: list[str] = []
    for number, line in enumerate(text.splitlines(), 1):
        if line.startswith("```"):
            if fence is None:
                fence = line[3:].strip()
                block = []
            else:
                if fence == "python":
                    try:
                        ast.parse("\n".join(block))
                    except SyntaxError as error:
                        errors.append(
                            f"{relative}:{number}: Python fence: {error.msg}"
                        )
                fence = None
            continue
        if fence is not None:
            block.append(line)
        indivisible = any(len(word) > 79 for word in line.split())
        if len(line) > 79 and not line.startswith("|") and not indivisible:
            errors.append(f"{relative}:{number}: line exceeds 79 characters")
    if fence is not None:
        errors.append(f"{relative}: unclosed code fence")

    for link in markdown_links(text):
        parsed = urlsplit(link)
        if parsed.scheme or parsed.netloc:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if not parsed.path:
            target = path
        if not target.is_relative_to(root):
            errors.append(f"{relative}: link leaves bundle: {link}")
        elif not target.exists():
            errors.append(f"{relative}: missing link: {link}")
        elif parsed.fragment and target.suffix == ".md":
            target_text = target.read_text(encoding="utf-8")
            if unquote(parsed.fragment) not in markdown_anchors(target_text):
                errors.append(f"{relative}: missing anchor: {link}")
    return errors


def validate(root: Path) -> list[str]:
    """Validate maintained text files, excluding Git and local caches."""
    root = root.resolve()
    errors: list[str] = []
    documents: dict[Path, str] = {}
    ignored = {".git", ".venv", ".ruff_cache", "__pycache__"}
    for path in sorted(root.rglob("*")):
        if not path.is_file() or ignored.intersection(path.parts):
            continue
        relative = path.relative_to(root)
        raw = path.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{relative}: not UTF-8 text")
            continue
        if b"\r" in raw or raw.startswith(b"\xef\xbb\xbf"):
            errors.append(f"{relative}: CR or UTF-8 BOM found")
        if raw and not raw.endswith(b"\n"):
            errors.append(f"{relative}: missing final newline")
        if path.suffix == ".md":
            documents[path] = text
            errors.extend(check_markdown(path, text, root))
        elif path.suffix == ".py":
            try:
                ast.parse(text)
            except SyntaxError as error:
                errors.append(f"{relative}: {error}")
        elif path.suffix == ".toml":
            try:
                tomllib.loads(text)
            except tomllib.TOMLDecodeError as error:
                errors.append(f"{relative}: {error}")

    references = root / "skills/pydemia-coding-style/references"
    entries: list[str] = []
    for name in ("python.md", "design.md", "workflow.md", "languages.md"):
        text = documents.get(references / name, "")
        sections = re.split(r"^## ([A-Z]+-\d{3}) — ", text, flags=re.MULTILINE)
        for index in range(1, len(sections), 2):
            entry, body = sections[index:index + 2]
            entries.append(entry)
            required = ("- 상태: ", "- 적용 범위: ", "- 근거: ")
            if not all(field in body for field in required):
                errors.append(f"{name}: missing metadata for {entry}")
            if "**이유:**" not in body or "**예외·한계:**" not in body:
                errors.append(
                    f"{name}: missing rationale or limits for {entry}"
                )
    duplicates = [key for key, count in Counter(entries).items() if count > 1]
    if duplicates:
        errors.append(f"duplicate convention IDs: {duplicates}")
    index_text = documents.get(references / "dictionary.md", "")
    indexed = re.findall(r"\[([A-Z]+-\d{3})\]", index_text)
    if not entries or Counter(entries) != Counter(indexed):
        errors.append("dictionary index does not match the convention entries")
    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Bundle validation passed: text, links, IDs, TOML, Python syntax.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
