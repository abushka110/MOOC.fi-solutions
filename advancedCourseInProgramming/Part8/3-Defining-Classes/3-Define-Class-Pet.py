# solution
class Pet:
    def __init__(self, name: str, species: str, year_of_birth: int):
        self.name = name
        self.species = species
        self.year_of_birth = year_of_birth

def new_pet(name_new: str, species_new: str, year_of_birth_new: int):
    return Pet(name_new, species_new, year_of_birth_new)

# test
if __name__ == "__main__":
    fluffy = new_pet("Fluffy", "dog", 2017)
    print(fluffy.name)
    print(fluffy.species)
    print(fluffy.year_of_birth)
    # Sample output
    # Fluffy
    # dog
    # 2017