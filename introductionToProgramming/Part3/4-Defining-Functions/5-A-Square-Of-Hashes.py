def hash_square(columns):
    rows = columns
    while columns != 0:
        print("#" * rows)
        columns -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    hash_square(5)