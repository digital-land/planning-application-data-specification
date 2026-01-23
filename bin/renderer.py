from pathlib import Path
from typing import Any, Dict

from utils import ensure_dir


def url_for(base_url: str, path: str) -> str:
    if not base_url:
        return "/" + path.lstrip("/")
    return base_url.rstrip("/") + "/" + path.lstrip("/")


def write_page(output_dir: Path, relative_path: str, content: str) -> None:
    target = output_dir / relative_path
    ensure_dir(target.parent)
    target.write_text(content, encoding="utf-8")


class RenderContext:
    def __init__(self, env, base_url: str, output_dir: Path):
        self.env = env
        self.base_url = base_url.rstrip("/")
        self.output_dir = output_dir

    def url_for(self, path: str) -> str:
        return url_for(self.base_url, path)

    def render(self, template_name: str, context: Dict[str, Any]) -> str:
        return self.env.get_template(template_name).render(**context)

    def write_page(self, relative_path: str, content: str) -> None:
        write_page(self.output_dir, relative_path, content)
