# solution
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
    numbers = []
    number_pool = list(range(lower, upper))
    numbers = sorted(sample(number_pool, amount))
    return numbers

# test
if __name__ == "__main__":
    for number in lottery_numbers(7, 1, 40):
        print(number)
