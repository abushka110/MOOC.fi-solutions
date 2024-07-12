import os

class Recipe:
    def __init__(self, name, ingredients, time, instructions):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def __str__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"

class RecipeBook:
    def __init__(self):
        self.recipes = []
        self.load_recipes()

    def add_recipe(self, recipe):
        if not any(r.name == recipe.name for r in self.recipes):
            self.recipes.append(recipe)
            self.save_recipes()
            print(f"Added recipe {recipe.name}")
        else:
            print("Recipe already exists")

    def remove_recipe(self, name):
        for i, recipe in enumerate(self.recipes):
            if recipe.name == name:
                del self.recipes[i]
                self.save_recipes()
                print(f"Removed recipe {name}")
                return
        print(f"No recipe found with name {name}")

    def find_recipe_by_name(self, name):
        for recipe in self.recipes:
            if recipe.name == name:
                print(f"Found recipe: {recipe}")
                return
        print(f"No recipe found with name {name}")

    def find_recipes_by_ingredient(self, ingredients):
        found = False
        for recipe in self.recipes:
            if all(ingredient in recipe.ingredients for ingredient in ingredients):
                print(recipe)
                found = True
        if not found:
            print(f"No recipe found with ingredients {ingredients}")

    def find_recipes_by_time(self, time):
        found = False
        for recipe in self.recipes:
            if recipe.time <= time:
                print(recipe)
                found = True
        if not found:
            print(f"No recipe found with preparation time {time} min")

    def list_all_recipes(self):
        if self.recipes:
            print("Found recipes:")
            for recipe in self.recipes:
                print(recipe)
        else:
            print("No recipes found")

    def clear_memory(self):
        self.recipes = []
        self.save_recipes()
        print("Memory cleared (All recipes deleted)")

    def load_recipes(self):
        if os.path.exists("recipes.txt"):
            with open("recipes.txt", "r") as file:
                for line in file:
                    name, ingredients, time, instructions = line.strip().split(";")
                    self.recipes.append(Recipe(name, ingredients.split(","), int(time), instructions))

    def save_recipes(self):
        with open("recipes.txt", "w") as file:
            for recipe in self.recipes:
                file.write(f"{recipe.name};{','.join(recipe.ingredients)};{recipe.time};{recipe.instructions}\n")

def main():
    recipe_book = RecipeBook()
    print("Recipe book program")
    commands = """
Commands:
0 - Exit
1 - Add recipe
2 - Remove recipe
3 - Search recipe by name
4 - Search recipe by ingredients
5 - Search recipe by preparation time
6 - Search recipe by available ingredients
7 - Return all recipes
8 - Clear memory
"""
    print(commands)
    while True:
        command = input("Enter command: ")
        if command == "0":
            break
        elif command == "1":
            name = input("Enter recipe name: ")
            time = int(input("Enter recipe cooktime (min): "))
            ingredients = input("Enter recipe ingredients separated by comma: ").split(",")
            instructions = input("Enter recipe instructions: ")
            recipe_book.add_recipe(Recipe(name, ingredients, time, instructions))
        elif command == "2":
            name = input("Enter name of recipe to remove: ")
            recipe_book.remove_recipe(name)
        elif command == "3":
            name = input("Enter recipe name to search: ")
            recipe_book.find_recipe_by_name(name)
        elif command == "4":
            ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ").split(",")
            recipe_book.find_recipes_by_ingredient(ingredients)
        elif command == "5":
            time = int(input("Enter the preparation time of the recipe you're looking for (min): "))
            recipe_book.find_recipes_by_time(time)
        elif command == "6":
            ingredients = input("Enter the ingredients of the recipe you're looking for, separated by commas: ").split(",")
            recipe_book.find_recipes_by_ingredient(ingredients)
        elif command == "7":
            recipe_book.list_all_recipes()
        elif command == "8":
            recipe_book.clear_memory()
        else:
            print(commands)

if __name__ == "__main__":
    main()