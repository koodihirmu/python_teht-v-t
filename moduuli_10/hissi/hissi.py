class Hissi:
    def __init__(self, lowestFloor: int, highestFloor: int) -> None:
        self.lowestFloor = lowestFloor
        self.highestFloor = highestFloor
        self.currentFloor = 0

    def moveTofloor(self, floor: int) -> None:
        # if the elevator is already at the floor
        if self.currentFloor == floor:
            print(f"Already at {floor}")
        # check if the floor exists
        elif floor > self.highestFloor or floor < self.lowestFloor:
            print(f"Floor {floor} doesn't exist in this house.")
        else:
            while self.currentFloor != floor:
                if self.currentFloor < floor:
                    self.floorUp()
                else:
                    self.floorDown()

    # go floor up when current floor is smaller than highest floor
    def floorUp(self) -> None:
        if self.currentFloor < self.highestFloor:
            print("Going a floor up")
            self.currentFloor += 1
        else:
            print("Already at the highest floor")
        print(f"Elevator is at floor: {self.currentFloor}")

    # go floor down when current floor is higher than lowest floor
    def floorDown(self) -> None:
        if self.currentFloor > self.lowestFloor:
            print("Going a floor down")
            self.currentFloor -= 1
        else:
            print("Already at the lowest floor")
        print(f"Elevator is at floor: {self.currentFloor}")

    # print all the data about the elevator
    def printData(self) -> None:
        print(
            f"Current Floor: {self.currentFloor}\nLowest Floor: {self.lowestFloor}\nHighest Floor: {self.highestFloor}"
        )
