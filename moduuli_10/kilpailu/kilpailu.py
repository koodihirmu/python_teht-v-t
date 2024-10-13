import random
from typing import List

from auto.auto import Auto


class Kilpailu:
    def __init__(self, name: str, length_km: int, cars: List[Auto]) -> None:
        self.name = name
        self.length_km = length_km
        self.cars: List[Auto] = cars
        self.winner = None
        self.duration = 0

    def hourPasses(self) -> None:
        self.duration += 1
        for car in self.cars:
            car.accelerate(random.uniform(-10, 15))
            car.drive(1.0)

    def printPositions(self) -> None:
        for car in self.cars:
            # check if the car won
            if car == self.winner:
                print(
                    f"WINNER Car {car.reg_number} speed is {car.current_speed}/{car.top_speed} and it has travelled {car.travelled_distance}"
                )
            else:
                print(
                    f"Car {car.reg_number} speed is {car.current_speed}/{car.top_speed} and it has travelled {car.travelled_distance}"
                )

    def competitionOver(self) -> bool:
        # check if a car has travelled to the goal
        for car in self.cars:
            if car.travelled_distance > self.length_km:
                self.winner = car
                return True
        return False
