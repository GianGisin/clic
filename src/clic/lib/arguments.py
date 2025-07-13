import pathlib, argparse
from .settings import params


def parse_args() -> tuple[pathlib.Path, params]:
    parser = argparse.ArgumentParser(
        prog="Custom Line Counter",
        description="Count lines of code in a file or project",
        epilog="(C) 2025 Gian Gisin",
    )
    parser.add_argument("filepath")
    parser.add_argument("-s", "--comment-symbol")
    parser.add_argument("-e", "--extension")
    parser.add_argument("-w", "--count-whitespace", action="store_true")
    parser.add_argument("-c", "--count-comments", action="store_true")

    args = parser.parse_args()

    path = pathlib.Path(args.filepath)

    suffix = set()

    if args.extension:
        suffix.add(args.extension)

    elif path.is_file():
        suffix.add(path.suffix)

    else:
        raise argparse.ArgumentError(
            None, message="File extension to search must be specified using -e"
        )

    if not args.comment_symbol:
        raise argparse.ArgumentError(
            None, message="You must include the comment symbol using -s"
        )

    s = params(
        args.comment_symbol,
        set(suffix),
        count_comments=args.count_comments,
        count_whitespaces=args.count_whitespace,
    )
    return (path, s)
