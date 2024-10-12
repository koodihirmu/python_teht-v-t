import random
from typing import List

from auto.auto import Auto


def main() -> None:
    # getting better typing from the library
    autos: List[Auto] = []
    # initialize all the cars in the competition
    for _ in range(10):
        auto = Auto(random.randint(100, 200))
        autos.append(auto)

    auto = Auto(random.randint(100, 200), reg_number="HAHA-123")
    autos.append(auto)

    # put the first car as the winning
    winning_car = autos[0]
    while winning_car.travelled_distance < 10000:
        # update all cars
        for auto in autos:
            # get random uniform float for the acceleration
            auto.accelerate(random.uniform(-10, 15))
            # update travelled_distance
            auto.drive(1.0)
            # check if current car is ahead
            if auto.travelled_distance > winning_car.travelled_distance:
                winning_car = auto.travelled_distance
                winning_car = auto

    for auto in autos:
        auto.print()
        input("Press Enter To Continue...")


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
