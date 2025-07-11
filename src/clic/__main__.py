import sys, os
from enum import Enum

from .lib.settings import params
from .lib.counter import count


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("Expected at least one argument: file path")
        sys.exit(os.EX_USAGE)

    # TODO: make relative paths possible
    count_path = args[1]
    # TODO: how to differentiate between folder search and a single file?
    # If a file path is passed in, set the file_extension to the extension of the file
    print(
        f"Total Lines: {count(count_path, params(comment_symbol="#", file_extensions=(".py",)))}"
    )


if __name__ == "__main__":
    main()
