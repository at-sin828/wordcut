"""Wrap text on spaces without breaking words."""
from __future__ import annotations


def wrap(text: str, width: int) -> list[str]:
    if width < 1:
        raise ValueError("宽度至少为 1")
    words = (text or "").split()
    if not words:
        return []
    lines: list[str] = []
    current = words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) <= width:
            current = f"{current} {word}"
        else:
            lines.append(current)
            current = word
    lines.append(current)
    return lines
