class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.__name = name
        self.__ingredients = ingredients
        self.__time = time
        self.__instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"

    # Getter methods
    @property
    def name(self):
        return self.__name
    
    @property
    def ingredients(self):
        return self.__ingredients
    
    @property
    def time(self):
        return self.__time
    
    @property
    def instructions(self):
        return self.__instructions
    
    # Setter method for name
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and len(new_name) >= 3:
            self.__name = new_name

    # Comparison operators for time
    def __lt__(self, other):
        return self.__time < other.__time

    def __gt__(self, other):
        return self.__time > other.__time
    
    def __le__(self, other):
        return self.__time <= other.__time

    def __ge__(self, other):
        return self.__time >= other.__time

    def __eq__(self, other):
        return self.__time == other.__time

    
    

if __name__ == "__main__":
    # test 1
    # r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken. Add salt.")
    # print(r1.name)

    # r1.name = "Delicious Chicken"
    # print("Name changed")
    # print("New name:", r1.name)

    # r1.name = "DC"
    # print("Name changed")
    # print("Name did not change, still:", r1.name)
    # r1.name = 123
    # print("Name can't be changed to other than string, so it's still:", r1.name)

    # try:
    #     r1.time = 5
    # except AttributeError:
    #     print("Time cannot be changed")

    # try:
    #     r1.ingredients = ["Chicken", "Salt", "Pepper"]
    # except AttributeError:
    #     print("Ingredients cannot be changed")

    # try:
    #     r1.instructions = "Fry the chicken. Add salt and pepper." 
    # except AttributeError:
    #     print("Instructions cannot be changed")


    # test 2
    r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken in a pan. Add salt.")
    r2 = Recipe("Caesar Salad", ["Lettuce", "Chicken", "Dressing"], 25, "Cook the chicken. Put the lettuce on a plate. Add chicken. Add dressing.")

    print("r1 > r2:", r1 > r2)
    print("r1 < r2:", r1 < r2)