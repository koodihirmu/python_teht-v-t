class Auto:
    def __init__(self, reg_number: str, top_speed: float) -> None:
        self.reg_number: str = reg_number
        self.top_speed: float = top_speed
        self.current_speed: float = 0
        self.travelled_distance: float = 0.0

    def print(self) -> None:
        print(
            f"""Registry number: {self.reg_number}\nTop speed: {self.top_speed:.0f}\nCurrent speed: {self.current_speed:.0f}\nTravelled_distance: {self.travelled_distance:.0f}\n \
        """
        )


def main() -> None:
    auto = Auto("ABC-123", 142)
    auto.print()


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
