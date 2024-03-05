# solution
def store_personal_data(person: tuple):
    with open("people.csv", "w") as file:
        file.write(f"{person[0]};{person[1]};{person[2]}\n")

# test
if __name__ == "__main__":
    store_personal_data(("Paul Paulson", 37, 175.5))
