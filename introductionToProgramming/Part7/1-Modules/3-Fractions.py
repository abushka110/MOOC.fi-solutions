# solution
from fractions import Fraction
def fractionate(amount: int):
    fraction_amount = Fraction(1, amount)
    return [fraction_amount] * amount

# test
if __name__ == "__main__":
    for p in fractionate(3):
        print(p)

    print()

    print(fractionate(5))

    # should print out:
    # 1/3
    # 1/3
    # 1/3

    # [Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5), Fraction(1, 5)]