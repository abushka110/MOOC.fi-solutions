# solution
from math import sqrt

def square_roots(origin_list: list) -> list:
    return [sqrt(item) for item in origin_list]

# test
if __name__ == "__main__":
    lines = square_roots([1,2,3,4])
    for line in lines:
        print(line)
    # expected output:
    # 1.0
    # 1.4142135623730951
    # 1.7320508075688772
    # 2.0