import random


class Dice:
    def roll_dice(self):
        d = [1, 2, 3, 4, 5, 6]
        first = 0
        second = 0
        for num in range(1, 6):
            first = random.choice(d)
            second = random.choice(d)

        return first, second

    def roll_dice_randomly(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

