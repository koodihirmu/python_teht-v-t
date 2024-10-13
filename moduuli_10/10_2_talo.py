from talo.talo import Talo


def main():
    talo = Talo(0, 8, 2)
    talo.driveElevator(7, 0)
    talo.driveElevator(7, 1)
    talo.driveElevator(7, 3)
    talo.driveElevator(7, -1)


if __name__ == "__main__":
    main()
    input("press enter to continue...")
