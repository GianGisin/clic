from typing import TextIO

from .settings import params


def _counts_as_line(line: str, settings: params) -> bool:
    line_clean = line.strip()
    if settings.count_comments and line_clean.startswith(settings.comment_symbol):
        return True

    if settings.count_whitespaces and line_clean == "":
        return True

    if line_clean and not line_clean.startswith(settings.comment_symbol):
        return True

    return False


def count_lines(file: TextIO, settings: params) -> int:
    lines = file.readlines()
    counter = 0
    for l in lines:
        if _counts_as_line(l, settings):
            counter += 1

    return counter
