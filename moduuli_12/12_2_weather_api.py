import sys

from location.location import Location


def main() -> None:
    try:
        location = Location(input("Give location for weather search: "))
        location.print_weather()
    except Exception as e:
        if __debug__:
            print(e)
        else:
            print("Error Happened")
            sys.exit(1)


if __name__ == "__main__":
    main()
    input("press enter ...")
