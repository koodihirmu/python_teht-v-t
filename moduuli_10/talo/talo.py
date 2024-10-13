from typing import List

from hissi.hissi import Hissi


class Talo:
    def __init__(self, lowestFloor: int, highestFloor: int, hisseja: int) -> None:
        self.lowestFloor = lowestFloor
        self.highestFloor = highestFloor

        # create list of elevators
        self.hissit: List[Hissi] = []
        # initialize the list with elevators
        for _ in range(hisseja):
            new_hissi = Hissi(self.lowestFloor, self.highestFloor)
            self.hissit.append(new_hissi)

    def driveElevator(self, floor: int, hissi_id: int) -> None:
        if hissi_id < 0:
            print("Elevator id negative")
            return
        try:
            self.hissit[hissi_id].moveTofloor(floor)
        except:
            print("Invalid elevator id")
            return
