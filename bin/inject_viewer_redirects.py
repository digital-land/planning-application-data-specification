"""Preserve old site URLs by adding redirects to their replacement pages."""

import argparse
import html
import json
from pathlib import Path
import re
from urllib.parse import quote

DESTINATION = "https://digital-land.github.io/planning-application-specification-viewer/"
START = "<!-- viewer-redirect:start -->"
END = "<!-- viewer-redirect:end -->"
NOTICE = "Do not delete this page: it preserves established links by redirecting to the replacement viewer."


def inject(content: str, relative_path: str) -> str:
    """Replace our marked blocks only, leaving the existing page intact."""
    content = re.sub(r"\n?" + re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", content, flags=re.S)
    path = relative_path.removesuffix("index.html") if relative_path.endswith("/index.html") or relative_path == "index.html" else relative_path
    target = DESTINATION + quote(path, safe="/")
    escaped = html.escape(target, quote=True)
    head = f'''{START}
<!-- {NOTICE} -->
<link rel="canonical" href="{escaped}">
<script>
window.location.replace({json.dumps(target)} + window.location.search + window.location.hash);
</script>
<noscript><meta http-equiv="refresh" content="0; url={escaped}"></noscript>
{END}
'''
    body = f'''{START}
<p role="status">This page has moved. <a href="{escaped}">View this page on the new specification viewer</a>.</p>
{END}
'''
    if not re.search(r"<head\b[^>]*>", content, re.I) or not re.search(r"<body\b[^>]*>", content, re.I):
        raise ValueError(f"Missing head or body in {relative_path}")
    # Refuse conflicting canonical declarations rather than silently publishing two.
    if re.search(r'<link\b[^>]*\brel=[\"\']canonical[\"\']', content, re.I):
        raise ValueError(f"Existing canonical link in {relative_path}")
    content = re.sub(r"(<head\b[^>]*>)", lambda m: m[1] + "\n" + head, content, count=1, flags=re.I)
    return re.sub(r"(<body\b[^>]*>)", lambda m: m[1] + "\n" + body, content, count=1, flags=re.I)


def inject_site(directory: Path) -> int:
    pages = sorted(directory.rglob("*.html"))
    if not pages:
        raise ValueError(f"No HTML pages found in {directory}")
    # Validate all pages before writing any of them.
    changes = [(p, inject(p.read_text(encoding="utf-8"), p.relative_to(directory).as_posix())) for p in pages]
    for path, content in changes:
        path.write_text(content, encoding="utf-8")
    return len(changes)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("docs"))
    args = parser.parse_args()
    print(f"Added viewer redirects to {inject_site(args.output)} HTML pages")


if __name__ == "__main__":
    main()
