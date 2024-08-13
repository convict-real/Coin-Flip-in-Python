from enum import Enum
import random

class Side(Enum):
    HEADS: int = 1
    TAILS: int = 2

def main():
    print("Type 'run' to flip")
    choice = input("Input: ")

    if choice != "run":
        print(f"Invalid choice: {choice}")
        return

    chance = random.random() * 100

    random_number = random.randint(1, 6000)
    side = Side((random_number - 1) // 2000 + 1)

    # Did this instead of adding it to Side because '1 / 6000' is near the actual chance of a coin landing on the edge, or in other words, I'm trying to make it realistic
    if (chance < 1 / 6000):
        print("It landed on the edge!")
        main()
    else:
        if side == Side.HEADS:
            print("It landed on heads!")
        elif side == Side.TAILS:
            print("It landed on tails!")

    exit(0)

if __name__ == "__main__":
    main()
