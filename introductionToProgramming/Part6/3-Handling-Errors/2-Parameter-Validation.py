# solution
def new_person(name: str, age: int):
    try:
        if name == "":
            raise Exception("name is an empty string")
        elif len(name.split(" ")) < 2:
            raise Exception("name contains less than two words")
        elif len(name) > 40:
            raise Exception("name is longer than 40 characters")
        elif age < 0:
            raise Exception("age is a negative number")
        elif age > 150:
            raise Exception("age is greater than 150")
        else:
            return (name, age)
    except ValueError:
        raise ValueError


# test
if __name__ == "__main__":
    print(new_person('James Jameson', 160))
