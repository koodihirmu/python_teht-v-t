from hissi.hissi import Hissi


def main():
    hissi = Hissi(0, 6)
    hissi.moveTofloor(3)
    hissi.moveTofloor(0)
    hissi.printData()


if __name__ == "__main__":
    main()
    input("press enter to continue...")
