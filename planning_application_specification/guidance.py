from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import frontmatter

GuidanceKey = tuple[str, str, str | None]
GuidanceIndex = dict[GuidanceKey, "Guidance"]


@dataclass(frozen=True)
class Guidance:
    content: str
    field: str | None = None
    dataset: str | None = None
    module: str | None = None
    component: str | None = None


def load_guidance(root: Path) -> GuidanceIndex:
    guidance_index: GuidanceIndex = {}
    guidance_root = root / "specification" / "guidance"

    for container_type in ("dataset", "module", "component"):
        container_root = guidance_root / container_type
        for container_path in sorted(container_root.glob("*")):
            if not container_path.is_dir():
                continue

            container_ref = container_path.name
            container_guidance = container_path / "index.md"
            if container_guidance.exists():
                _add_guidance(
                    guidance_index,
                    container_guidance,
                    container_type,
                    container_ref,
                )

            for path in sorted((container_path / "field").glob("*.md")):
                _add_guidance(
                    guidance_index,
                    path,
                    container_type,
                    container_ref,
                    field=path.stem,
                )

    return guidance_index


def _add_guidance(
    guidance_index: GuidanceIndex,
    path: Path,
    container_type: str,
    container_ref: str,
    field: str | None = None,
) -> None:
    post = frontmatter.load(path)
    metadata_container = str(post.get(container_type, "")).strip()
    metadata_field = str(post.get("field", "")).strip() or None

    if metadata_container != container_ref or metadata_field != field:
        raise ValueError(f"Guidance metadata does not match its path: {path}")

    context = {
        "dataset": None,
        "module": None,
        "component": None,
    }
    context[container_type] = container_ref
    key = (container_type, container_ref, field)
    guidance_index[key] = Guidance(
        content=post.content.strip(),
        field=field,
        **context,
    )
