# File to be used as test for counting
# Including Comments: 13 lines
def do_something() -> None:
    for i in range(40):
        print(f"doing nothing the {i+1}th time")


def main() -> None:
    do_something()


if __name__ == "__main__":
    main()
