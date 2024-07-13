# solution
def prime_numbers():
    number = 2

    while True:
        if is_prime(number):
            yield number
        number += 1

# function that checks if the number is prime or not
def is_prime(number: int):
        for i in range(2, number-1):
            if number % i == 0:
                return False
        
        return True

# test
if __name__ == "__main__":
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
    # expected output:
    # 2
    # 3
    # 5
    # 7
    # 11
    # 13
    # 17
    # 19