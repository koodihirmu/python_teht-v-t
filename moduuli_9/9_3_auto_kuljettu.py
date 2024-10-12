from auto.auto import Auto


def main() -> None:
    auto = Auto(142, "ABC-123")
    auto.travelled_distance = 2000
    auto.accelerate(60)
    auto.drive(1.5)
    auto.print()


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
