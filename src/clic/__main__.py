import sys, os

from .lib.count_file import count_lines
from .lib.settings import params


def main() -> None:
    args = sys.argv
    if len(args) < 2:
        print("Expected at least one argument: file path")
        sys.exit(os.EX_USAGE)

    file_path = args[1]
    print(sys.argv)
    with open(file_path, "r") as f:
        print(f"Lines in the file: {count_lines(f, params("#"))}")


if __name__ == "__main__":
    main()
