class Recipe:
    def __init__(self, name: str, ingredients: list, time: int, instructions: str):
        self.name = name
        self.ingredients = ingredients
        self.time = time
        self.instructions = instructions

    def __repr__(self):
        return f"Recipe(name='{self.name}', ingredients={self.ingredients}, time={self.time}, instructions='{self.instructions}')"

class RecipeBook:
    def __init__(self):
        self.__recipe_book = []

    def __str__(self):
        result = "RecipeBook:\n"
        result += "\n".join([str(recipe) for recipe in self.__recipe_book])
        return result

    def add_recipe(self, recipe: Recipe):
        self.__recipe_book.append(recipe)

    def remove_recipe(self, recipe: Recipe):
        self.__recipe_book.remove(recipe)

    def recipe_by_name(self, name: str):
        for recipe_inside in self.__recipe_book:
            if recipe_inside.name == name:
                return recipe_inside
        return None
    
    def recipes_containing_ingredients(self, ingredients: list):
        result = []
        for recipe in self.__recipe_book:
            contains_all = True
            for ingredient in ingredients:
                if ingredient not in recipe.ingredients:
                    contains_all = False
                    break
            if contains_all:
                result.append(recipe)
        return result
    
    def recipes_within_time(self, time: int):
        result = [recipe for recipe in self.__recipe_book if recipe.time <= time]
        return result
    
    def recipes_with_all_ingredients(self, ingredients: list):
        result = []
        for recipe in self.__recipe_book:
            if all(ingredient in ingredients for ingredient in recipe.ingredients):
                result.append(recipe)
        return result

    def all_recipes(self):
        return self.__recipe_book.copy()

if __name__ == "__main__":
    r1 = Recipe("Chicken", ["Chicken", "Salt"], 15, "Fry the chicken in a frying pan. Add salt.")
    r2 = Recipe("Caesar Salad", ["Lettuce", "Chicken", "Dressing"], 25, "Cook the chicken. Place lettuce on a plate. Add chicken. Add dressing.")
    r3 = Recipe("Blueberry Muffins", ["Flour", "Milk", "Sugar", "Blueberries"], 30, "Mix ingredients. Bake muffins at 180 degrees.")

    recipe_book = RecipeBook()
    recipe_book.add_recipe(r1)
    recipe_book.add_recipe(r2)
    recipe_book.add_recipe(r3)
    print(recipe_book)
    print()

    chicken = recipe_book.recipe_by_name("Chicken")
    print("Recipe with search 'Chicken':", chicken)
    print("Recipe with search 'Risotto':", recipe_book.recipe_by_name("Risotto"))
    print()

    recipes_with_ingredients = recipe_book.recipes_containing_ingredients(["Chicken", "Dressing"])
    print("Recipes that contain the ingredients 'Chicken', 'Dressing':", recipes_with_ingredients)
    print()

    recipes_can_be_made_with = recipe_book.recipes_with_all_ingredients(["Chicken", "Salt", "Dressing", "Lettuce"])
    print("Recipes that can be made with ingredients 'Chicken', 'Salt', 'Dressing', and 'Lettuce':", recipes_can_be_made_with)

    print()
    within_time = recipe_book.recipes_within_time(20)
    print(within_time)
    print("Recipes whose only ingredient is water:", recipe_book.recipes_with_all_ingredients(["Water"]))
    print("Recipes that can be made in one minute:", recipe_book.recipes_within_time(1))
    print()
    print("All known recipes:")
    print(recipe_book.all_recipes())