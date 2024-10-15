import random
from typing import List

from auto.auto import Auto, PolttomoottoriAuto, SahkoAuto


# updating cars and printing them recursively
def recursive_fun(autot: List[Auto], index: int) -> None:
    # try the index and if we are over the limit exit the loop and start printing away
    try:
        autot[index].accelerate(random.randint(100, 200))
        autot[index].drive(3)
        recursive_fun(autot, index + 1)
    except:
        return
    autot[index].print()


def main() -> None:
    sAuto = SahkoAuto(180, 52.5, "ABC-15")
    pAuto = PolttomoottoriAuto(165, 32.3, "ACD-123")

    autot: List[Auto] = [sAuto, pAuto]

    recursive_fun(autot, 0)


if __name__ == "__main__":
    main()
    input("press enter to continue...")
