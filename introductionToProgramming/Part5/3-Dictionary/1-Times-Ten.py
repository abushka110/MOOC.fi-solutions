# solution
def times_ten(start_index: int, end_index: int):
    ten_dictionary = {}
    for i in range(start_index, end_index + 1):
        ten_dictionary[i] = i * 10
    return ten_dictionary

# test
if __name__ == "__main__":
    d = times_ten(3, 6)
    print(d) # {3: 30, 4: 40, 5: 50, 6: 60}