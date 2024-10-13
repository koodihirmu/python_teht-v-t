class Auto:
    # giving the whole class an id field to calculate registry numbers
    id = 0

    def __init__(self, top_speed: float, reg_number: str = "DEFAULT") -> None:
        if reg_number == "DEFAULT":
            self.reg_number = f"ABC-{Auto.id}"
        else:
            self.reg_number: str = reg_number
        self.top_speed: float = top_speed
        self.current_speed: float = 0.0
        self.travelled_distance: float = 0.0
        Auto.id += 1

    def print(self) -> None:
        print(
            f"""Registry number: {self.reg_number}\nTop speed: {self.top_speed:.0f}\nCurrent speed: {self.current_speed:.0f}\nTravelled distance: {self.travelled_distance:.0f} \
        """
        )

    def accelerate(self, change_in_speed: float) -> None:
        if self.current_speed + change_in_speed < 0.0:
            # always + values minus sign is a scam
            self.current_speed = 0.0
            return
        elif self.current_speed + change_in_speed > self.top_speed:
            self.current_speed = self.top_speed
            return
        else:
            self.current_speed += change_in_speed

    def drive(self, time_h: float) -> None:
        # NOTE: vt = d
        self.travelled_distance += self.current_speed * time_h
