# using my own module Auto to make things neater in all of these
from auto.auto import Auto


def main() -> None:
    auto = Auto(142, "ABC-123")
    auto.print()


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
