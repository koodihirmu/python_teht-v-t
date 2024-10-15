from julkaisu.julkaisu import Kirja, Lehti


def main() -> None:
    lehti = Lehti("Aku Ankka", "Aki Hyyppä")
    kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

    lehti.print()
    kirja.print()


if __name__ == "__main__":
    main()
    input("press enter to continue...")
