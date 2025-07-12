import sys, os, pathlib

from .lib.settings import params
from .lib.counter import count


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("Expected at least one argument: file path")
        sys.exit(os.EX_USAGE)

    count_path = pathlib.Path(args[1]).expanduser()
    if not count_path.exists():
        print(f"The given path ('{count_path}') does not exist")
        sys.exit(os.EX_USAGE)

    suffixes = set()

    if count_path.is_file():
        suffixes.add(count_path.suffix)
    elif len(args) < 3:
        print("Please provide a file extension to search")
        sys.exit(os.EX_USAGE)
    else:
        suffixes.add(args[2])

    settings = params(comment_symbol="#", file_extensions=suffixes)

    print(f"Total Lines: {count(count_path, settings)}")


if __name__ == "__main__":
    main()
