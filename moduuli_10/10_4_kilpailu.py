import random
from typing import List

from auto.auto import Auto
from kilpailu.kilpailu import Kilpailu


def main():
    autos: List[Auto] = []
    # generate list of cars for the competition
    for _ in range(3):
        auto = Auto(random.randint(100, 200))
        autos.append(auto)

    suuriRomuralli = Kilpailu("Suuri romuralli", 8000, autos)

    while not suuriRomuralli.competitionOver():
        suuriRomuralli.hourPasses()
        if (suuriRomuralli.duration % 10 != 0) and suuriRomuralli.duration != 0:
            suuriRomuralli.printPositions()
    suuriRomuralli.printPositions()


if __name__ == "__main__":
    main()
    input("Press Enter To Continue...")
