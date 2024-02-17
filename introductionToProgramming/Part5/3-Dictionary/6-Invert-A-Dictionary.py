# solution
def invert(dictionary: dict):
    keys = list(dictionary.keys())
    for key_no in keys:
        value = dictionary.pop(key_no)
        dictionary[value] = key_no

# model solution
def invert(dictionary: dict):
	copy = {}
	for key in dictionary:
		copy[key] = dictionary[key]
	for key in copy:
		del dictionary[key]
	for key in copy:
		dictionary[copy[key]] = key

# test
if __name__ == "__main__":
    s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
    invert(s)
    print(s) # {"first": 1, "second": 2, "third": 3, "fourth": 4}

    s = {1: 10, 2: 20, 3: 30}
    invert(s)
    print(s) # {10: 1, 20: 2, 30: 3}