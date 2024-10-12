from auto.auto import Auto


def main() -> None:
    auto = Auto(142, "ABC-123")
    auto.print()
    auto.accelerate(30)
    auto.accelerate(70)
    auto.accelerate(50)
    auto.accelerate(-200)
    auto.print()


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
