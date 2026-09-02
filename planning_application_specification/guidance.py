from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import frontmatter


@dataclass(frozen=True)
class Guidance:
    field: str
    content: str
    dataset: str | None = None
    module: str | None = None
    component: str | None = None


def load_guidance(root: Path) -> dict[str, dict[str, Guidance]]:
    guidance_index: dict[str, dict[str, Guidance]] = {}
    pattern = root / "specification" / "guidance" / "dataset" / "*" / "field" / "*.md"

    for path in sorted(root.glob(str(pattern.relative_to(root)))):
        post = frontmatter.load(path)
        dataset = str(post.get("dataset", "")).strip()
        field = str(post.get("field", "")).strip()

        expected_dataset = path.parent.parent.name
        expected_field = path.stem
        if dataset != expected_dataset or field != expected_field:
            raise ValueError(f"Guidance metadata does not match its path: {path}")

        guidance_index.setdefault(dataset, {})[field] = Guidance(
            dataset=dataset,
            field=field,
            content=post.content.strip(),
        )

    return guidance_index
