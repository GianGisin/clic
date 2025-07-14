import pathlib
from .settings import params
from .count_file import count_lines


def count(path: pathlib.Path, settings: params) -> int:
    if path.is_file() and path.suffix == settings.file_extension:
        # print(f"Matched file: {str(path)}")
        with path.open() as f:
            return count_lines(f, settings)

    if path.is_dir():
        sub_total = 0
        for p in path.iterdir():
            sub_total += count(p, settings)

        return sub_total

    return 0
