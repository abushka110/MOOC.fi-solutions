# solution
def factorials(n: int):
    factorials_dict = {}
    factorials_dict[1] = 1
    for i in range(2, n + 1):
        factorials_dict[i] = factorials_dict[i - 1] * i
    return factorials_dict

# test
if __name__ == "__main__":
    k = factorials(5)
    print(k[1])
    print(k[3])
    print(k[5])