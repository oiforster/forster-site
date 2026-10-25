"""Le as paginas de design aprovadas; os metadados e a medicao ficam no gerador."""
import pathlib
import re
from html import unescape
from urllib.parse import urlsplit

PAGES = {
    "Home-2026-10-25.html": "/",
    "Acompanhamento-2026-10-25.html": "/acompanhamento",
    "Mentoria-2026-10-25.html": "/mentoria",
    "Sites-2026-10-25.html": "/sites",
    "Videos-2026-10-25.html": "/sob-encomenda",
    "Trabalhos-2026-10-25.html": "/trabalhos",
}


def load_design(path):
    source = pathlib.Path(path).read_text(encoding="utf-8")
    body = re.search(r"<body\b([^>]*)>([\s\S]*?)</body>", source, re.I)
    if not body:
        raise ValueError(f"Pagina de design sem body: {path}")
    styles = "\n".join(re.findall(r"<style\b[^>]*>([\s\S]*?)</style>", source, re.I))
    if not styles:
        raise ValueError(f"Pagina de design sem CSS: {path}")

    def local_attribute(match):
        value = unescape(match.group(3))
        parsed = urlsplit(value)
        name = parsed.path.rsplit("/", 1)[-1]
        if name in PAGES and (not parsed.netloc or "claudeusercontent.com" in parsed.netloc):
            value = PAGES[name] + ("#" + parsed.fragment if parsed.fragment else "")
        elif parsed.netloc == "somosforster.com.br":
            value = parsed.path or "/"
            if parsed.query:
                value += "?" + parsed.query
            if parsed.fragment:
                value += "#" + parsed.fragment
        elif value.endswith("/assets/img/temas-polaris.png"):
            value = "/img/temas-polaris.png"
        return match.group(1) + match.group(2) + value.replace("&", "&amp;") + match.group(2)

    content = re.sub(r"((?:href|src|srcset|poster)\s*=\s*)([\"'])(.*?)(?:\2)",
                     local_attribute, body.group(2), flags=re.I)
    head = re.search(r"<head\b[^>]*>([\s\S]*?)</head>", source, re.I)
    if head:
        scripts = re.findall(r"<script\b[^>]*>[\s\S]*?</script>", head.group(1), re.I)
        content += "\n" + "\n".join(s for s in scripts if "application/ld+json" not in s.lower())
    content = re.sub(r'<script\b[^>]*type=["\']application/ld\+json["\'][^>]*>[\s\S]*?</script>',
                     '', content, flags=re.I)
    # Links para outras paginas do proprio site seguem na mesma aba.
    content = re.sub(r'(<a\b[^>]*href=["\']/(?!/)[^>]*?)\s+target=["\']_blank["\']',
                     r"\1", content, flags=re.I)
    if re.search(r"(?:support\.js|data-dc-script|__DC_|/_ds/)", content):
        raise ValueError(f"Pagina contem dependencias de previa do Design: {path}")
    return {"css": styles, "body": content.strip(), "body_attrs": body.group(1).strip()}
