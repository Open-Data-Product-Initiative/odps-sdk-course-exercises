#!/usr/bin/env python3
"""Build a dependency-free static HTML package from repository Markdown files."""

from __future__ import annotations

import argparse
import html
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse


SKIP_DIRS = {".git", "html", "tests", "tools", "__pycache__", ".pytest_cache"}
STYLE = """
:root {
  color-scheme: light;
  --bg: #f6f8fb;
  --panel: #ffffff;
  --ink: #18212f;
  --muted: #5c6b80;
  --line: #dce3ed;
  --accent: #006f8f;
  --accent-strong: #004f66;
  --code-bg: #111827;
  --code-ink: #e5edf7;
}

* {
  box-sizing: border-box;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  font-size: 16px;
  line-height: 1.65;
}

a {
  color: var(--accent);
  text-decoration-thickness: 1px;
  text-underline-offset: 3px;
}

a:hover {
  color: var(--accent-strong);
}

.site {
  min-height: 100vh;
  display: grid;
  grid-template-columns: minmax(240px, 320px) minmax(0, 1fr);
}

.sidebar {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: auto;
  border-right: 1px solid var(--line);
  background: #ffffff;
  padding: 24px;
}

.brand {
  display: block;
  margin-bottom: 18px;
}

.brand img {
  width: 100%;
  max-width: 240px;
  border-radius: 8px;
  border: 1px solid var(--line);
  display: block;
}

.nav-title {
  color: var(--muted);
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  margin: 22px 0 8px;
  text-transform: uppercase;
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-list a {
  display: block;
  border-radius: 6px;
  color: var(--ink);
  font-size: 14px;
  line-height: 1.35;
  padding: 8px 10px;
  text-decoration: none;
}

.nav-list a:hover,
.nav-list a[aria-current="page"] {
  background: #e9f4f7;
  color: var(--accent-strong);
}

.content-wrap {
  padding: 40px clamp(20px, 5vw, 72px);
}

.content {
  background: var(--panel);
  border: 1px solid var(--line);
  border-radius: 8px;
  max-width: 980px;
  padding: clamp(24px, 4vw, 52px);
  box-shadow: 0 18px 45px rgba(24, 33, 47, 0.08);
}

.breadcrumbs {
  color: var(--muted);
  font-size: 13px;
  margin-bottom: 18px;
}

.breadcrumbs a {
  color: var(--muted);
}

h1,
h2,
h3,
h4 {
  line-height: 1.2;
  margin: 1.8em 0 0.55em;
}

h1 {
  font-size: 34px;
  margin-top: 0;
}

h2 {
  border-top: 1px solid var(--line);
  font-size: 24px;
  padding-top: 26px;
}

h3 {
  font-size: 19px;
}

p,
ul,
ol,
pre,
blockquote,
table {
  margin: 0 0 1.1em;
}

ul,
ol {
  padding-left: 1.4em;
}

li + li {
  margin-top: 0.25em;
}

code {
  background: #eef3f8;
  border: 1px solid #d8e1ec;
  border-radius: 4px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
  font-size: 0.92em;
  padding: 0.1em 0.28em;
}

pre {
  background: var(--code-bg);
  border-radius: 8px;
  color: var(--code-ink);
  overflow-x: auto;
  padding: 16px 18px;
}

pre code {
  background: transparent;
  border: 0;
  color: inherit;
  display: block;
  padding: 0;
}

blockquote {
  border-left: 4px solid var(--accent);
  color: var(--muted);
  margin-left: 0;
  padding-left: 16px;
}

img {
  height: auto;
  max-width: 100%;
}

.content > p:first-child img {
  border-radius: 8px;
  border: 1px solid var(--line);
}

hr {
  border: 0;
  border-top: 1px solid var(--line);
  margin: 28px 0;
}

@media (max-width: 860px) {
  .site {
    display: block;
  }

  .sidebar {
    height: auto;
    position: static;
  }

  .content-wrap {
    padding: 18px;
  }

  .content {
    padding: 24px 20px;
  }
}
""".strip()


def should_skip(path: Path) -> bool:
    return any(part in SKIP_DIRS or part.startswith(".") for part in path.parts)


def title_from_markdown(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    if path.name == "README.md":
        return path.parent.name or "Course Home"
    return path.stem.replace("-", " ").replace("_", " ").title()


def output_path_for_markdown(root: Path, source: Path, output_dir: Path) -> Path:
    rel = source.relative_to(root)
    if rel.name == "README.md":
        if rel.parent == Path("."):
            return output_dir / "index.html"
        return output_dir / rel.parent / "index.html"
    return output_dir / rel.with_suffix(".html")


def is_external_url(target: str) -> bool:
    parsed = urlparse(target)
    return bool(parsed.scheme or parsed.netloc) or target.startswith("#")


def split_target(target: str) -> tuple[str, str, str]:
    base = target
    anchor = ""
    query = ""
    if "#" in base:
        base, anchor = base.split("#", 1)
        anchor = "#" + anchor
    if "?" in base:
        base, query = base.split("?", 1)
        query = "?" + query
    return base, query, anchor


def rewrite_url(
    target: str,
    source_md: Path,
    source_html: Path,
    md_outputs: dict[Path, Path],
    asset_outputs: dict[Path, Path],
) -> str:
    if is_external_url(target):
        return target
    base, query, anchor = split_target(target)
    if base.startswith("html/"):
        packaged_target = source_html.parent / base.removeprefix("html/")
        return Path(os.path.relpath(packaged_target, source_html.parent)).as_posix() + query + anchor
    if not base:
        return query + anchor
    resolved = (source_md.parent / base).resolve()
    destination = None
    if resolved in md_outputs:
        destination = md_outputs[resolved]
    elif resolved in asset_outputs:
        destination = asset_outputs[resolved]
    if destination is None:
        return target
    rel = Path(os.path.relpath(destination, source_html.parent)).as_posix()
    return rel + query + anchor


def render_inline(
    text: str,
    source_md: Path,
    source_html: Path,
    md_outputs: dict[Path, Path],
    asset_outputs: dict[Path, Path],
) -> str:
    placeholders: list[str] = []

    def stash(value: str) -> str:
        placeholders.append(value)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def image_repl(match: re.Match[str]) -> str:
        alt = html.escape(match.group(1), quote=True)
        src = html.escape(
            rewrite_url(match.group(2), source_md, source_html, md_outputs, asset_outputs),
            quote=True,
        )
        return stash(f'<img src="{src}" alt="{alt}">')

    def link_repl(match: re.Match[str]) -> str:
        label = render_inline(match.group(1), source_md, source_html, md_outputs, asset_outputs)
        href = html.escape(
            rewrite_url(match.group(2), source_md, source_html, md_outputs, asset_outputs),
            quote=True,
        )
        return stash(f'<a href="{href}">{label}</a>')

    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", image_repl, text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, text)
    text = re.sub(r"`([^`]+)`", lambda m: stash(f"<code>{html.escape(m.group(1))}</code>"), text)
    text = html.escape(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)
    for index, value in enumerate(placeholders):
        text = text.replace(f"\u0000{index}\u0000", value)
    return text


def flush_paragraph(
    html_parts: list[str],
    paragraph: list[str],
    source_md: Path,
    source_html: Path,
    md_outputs: dict[Path, Path],
    asset_outputs: dict[Path, Path],
) -> None:
    if paragraph:
        text = " ".join(line.strip() for line in paragraph)
        html_parts.append(
            "<p>"
            + render_inline(text, source_md, source_html, md_outputs, asset_outputs)
            + "</p>"
        )
        paragraph.clear()


def normalize_wrapped_list_items(markdown: str) -> list[str]:
    normalized: list[str] = []
    in_code = False
    for raw_line in markdown.splitlines():
        stripped = raw_line.strip()
        if stripped.startswith("```"):
            in_code = not in_code
            normalized.append(raw_line)
            continue
        is_continuation = (
            not in_code
            and normalized
            and raw_line.startswith(("  ", "\t"))
            and stripped
            and re.match(r"^\s*(?:[-*]|\d+\.)\s+", normalized[-1])
            and not re.match(r"^\s*(?:[-*]|\d+\.)\s+", raw_line)
        )
        if is_continuation:
            normalized[-1] = normalized[-1].rstrip() + " " + stripped
        else:
            normalized.append(raw_line)
    return normalized


def render_markdown(
    markdown: str,
    source_md: Path,
    source_html: Path,
    md_outputs: dict[Path, Path],
    asset_outputs: dict[Path, Path],
) -> str:
    parts: list[str] = []
    paragraph: list[str] = []
    list_type: str | None = None
    in_code = False
    code_lang = ""
    code_lines: list[str] = []

    def close_list() -> None:
        nonlocal list_type
        if list_type:
            parts.append(f"</{list_type}>")
            list_type = None

    for raw_line in normalize_wrapped_list_items(markdown):
        line = raw_line.rstrip()
        if line.startswith("```"):
            if in_code:
                class_attr = f' class="language-{html.escape(code_lang, quote=True)}"' if code_lang else ""
                parts.append(
                    f"<pre><code{class_attr}>"
                    + html.escape("\n".join(code_lines))
                    + "</code></pre>"
                )
                in_code = False
                code_lang = ""
                code_lines = []
            else:
                flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
                close_list()
                in_code = True
                code_lang = line[3:].strip()
            continue
        if in_code:
            code_lines.append(raw_line)
            continue
        if not line.strip():
            flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
            close_list()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
            close_list()
            level = len(heading.group(1))
            text = render_inline(heading.group(2), source_md, source_html, md_outputs, asset_outputs)
            parts.append(f"<h{level}>{text}</h{level}>")
            continue
        unordered = re.match(r"^\s*[-*]\s+(.+)$", line)
        ordered = re.match(r"^\s*\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
            target_list = "ul" if unordered else "ol"
            if list_type != target_list:
                close_list()
                parts.append(f"<{target_list}>")
                list_type = target_list
            item = (unordered or ordered).group(1)
            parts.append(
                "<li>"
                + render_inline(item, source_md, source_html, md_outputs, asset_outputs)
                + "</li>"
            )
            continue
        quote = re.match(r"^>\s?(.*)$", line)
        if quote:
            flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
            close_list()
            parts.append(
                "<blockquote><p>"
                + render_inline(quote.group(1), source_md, source_html, md_outputs, asset_outputs)
                + "</p></blockquote>"
            )
            continue
        if line in {"---", "***", "___"}:
            flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
            close_list()
            parts.append("<hr>")
            continue
        paragraph.append(line)

    flush_paragraph(parts, paragraph, source_md, source_html, md_outputs, asset_outputs)
    close_list()
    if in_code:
        parts.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
    return "\n".join(parts)


def nav_items(root: Path, md_files: list[Path], md_outputs: dict[Path, Path], current: Path) -> str:
    ordered = sorted(
        (path for path in md_files if path.name == "README.md"),
        key=lambda path: (path.relative_to(root) != Path("README.md"), path.relative_to(root).as_posix()),
    )
    items = []
    for source in ordered:
        destination = md_outputs[source.resolve()]
        rel = Path(os.path.relpath(destination, current.parent)).as_posix()
        title = html.escape(title_from_markdown(source))
        current_attr = ' aria-current="page"' if destination == current else ""
        items.append(f'<li><a href="{rel}"{current_attr}>{title}</a></li>')
    return "\n".join(items)


def page_template(
    *,
    title: str,
    body: str,
    root: Path,
    current: Path,
    md_files: list[Path],
    md_outputs: dict[Path, Path],
) -> str:
    css = (root / "html" / "assets" / "style.css").resolve()
    cover = (root / "html" / "assets" / "cover.png").resolve()
    css_rel = Path(os.path.relpath(css, current.parent)).as_posix()
    cover_rel = Path(os.path.relpath(cover, current.parent)).as_posix()
    home = Path(os.path.relpath((root / "html" / "index.html").resolve(), current.parent)).as_posix()
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)} | Open Data Products SDK Course</title>
  <link rel="stylesheet" href="{css_rel}">
</head>
<body>
  <div class="site">
    <aside class="sidebar">
      <a class="brand" href="{home}"><img src="{cover_rel}" alt="Open Data Products SDK course cover"></a>
      <div class="nav-title">Course Material</div>
      <ul class="nav-list">
{nav_items(root, md_files, md_outputs, current)}
      </ul>
    </aside>
    <main class="content-wrap">
      <article class="content">
        <div class="breadcrumbs"><a href="{home}">Course home</a></div>
{body}
      </article>
    </main>
  </div>
</body>
</html>
"""


def discover_markdown(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.rglob("*.md")
        if not should_skip(path.relative_to(root))
    )


def discover_assets(root: Path, output_dir: Path) -> dict[Path, Path]:
    assets: dict[Path, Path] = {}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if path.is_dir() or should_skip(rel) or path.suffix == ".md":
            continue
        if rel == Path("cover.png"):
            assets[path.resolve()] = (output_dir / "assets" / "cover.png").resolve()
        else:
            assets[path.resolve()] = (output_dir / rel).resolve()
    return assets


def build_site(root: Path, output_dir: Path) -> None:
    root = root.resolve()
    output_dir = output_dir.resolve()
    if output_dir.exists():
        shutil.rmtree(output_dir)
    (output_dir / "assets").mkdir(parents=True, exist_ok=True)
    (output_dir / "assets" / "style.css").write_text(STYLE + "\n", encoding="utf-8")

    md_files = discover_markdown(root)
    md_outputs = {
        source.resolve(): output_path_for_markdown(root, source, output_dir).resolve()
        for source in md_files
    }
    asset_outputs = discover_assets(root, output_dir)

    for source, destination in asset_outputs.items():
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)

    for source in md_files:
        source_resolved = source.resolve()
        destination = md_outputs[source_resolved]
        destination.parent.mkdir(parents=True, exist_ok=True)
        markdown = source.read_text(encoding="utf-8")
        title = title_from_markdown(source)
        body = render_markdown(markdown, source_resolved, destination, md_outputs, asset_outputs)
        page = page_template(
            title=title,
            body=body,
            root=root,
            current=destination,
            md_files=md_files,
            md_outputs=md_outputs,
        )
        destination.write_text(page, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Build the static HTML course package.")
    parser.add_argument("--root", default=".", help="Repository root. Defaults to current directory.")
    parser.add_argument("--output", default="html", help="Output folder. Defaults to html/.")
    args = parser.parse_args()
    root = Path(args.root)
    output = root / args.output
    build_site(root, output)
    print(f"Built HTML package at {output}")


if __name__ == "__main__":
    main()
