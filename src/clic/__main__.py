import sys, argparse

from .lib.counter import count
from .lib.arguments import parse_args


def main() -> None:
    try:
        count_path, settings = parse_args()
    except argparse.ArgumentError as e:
        print(f"Error parsing args: {e.message}")
        sys.exit(1)

    print(f"Total Lines: {count(count_path, settings)}")


if __name__ == "__main__":
    main()
