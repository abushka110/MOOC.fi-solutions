# solution
def new_person(name: str, age: int):
    if name == "" or len(name.split(" ")) < 2 or len(name) > 40:
        raise ValueError
    if age < 0 or age > 150:
        raise ValueError
    return (name, age)


# test
if __name__ == "__main__":
    print(new_person('James Jameson', 160))
