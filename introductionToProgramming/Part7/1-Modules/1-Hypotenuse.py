# solution
from math import sqrt
def hypotenuse(leg1: float, leg2: float):
    leg3 = (leg1 ** 2) + (leg2 ** 2)
    leg3 = sqrt(leg3)
    return leg3

# model solution
# from math import sqrt
# def hypotenuse(leg1: float, leg2: float):
#     return sqrt((leg1 ** 2) + (leg2 ** 2))

# test
if __name__ == "__main__":
    print(hypotenuse(3,4)) # 5.0
    print(hypotenuse(5,12)) # 13.0
    print(hypotenuse(1,1)) # 1.4142135623730951
