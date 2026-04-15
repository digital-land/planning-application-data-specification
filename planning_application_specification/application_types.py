from __future__ import annotations

from typing import Iterable


def normalise_application_types(value: object) -> tuple[str, ...]:
    if value is None:
        return ()

    if isinstance(value, str):
        candidates: Iterable[object] = [value]
    elif isinstance(value, (list, tuple, set)):
        candidates = value
    else:
        return ()

    cleaned: list[str] = []
    for candidate in candidates:
        if not isinstance(candidate, str):
            continue
        for part in candidate.split(";"):
            item = part.strip()
            if item:
                cleaned.append(item)

    return tuple(sorted(set(cleaned)))


def canonical_application_ref(value: object) -> str:
    return ";".join(normalise_application_types(value))
