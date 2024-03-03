# solution
def copy_recipes(filename: str):
    prev_item = 0
    name = ""
    recipes = {}
    with open(filename) as file:
        for item in file:
            item = item.replace("\n", "")
            if item == "":
                prev_item = 0
            elif prev_item == 0:
                name = item
                recipes[name] = ""
                prev_item = 1
            elif prev_item == 1:
                prev_item = 2
                recipes[name] = [int(item), []]
            elif prev_item == 2:
                recipes[name][1].append(item)
    recipes_names = list(recipes.keys())
    return recipes, recipes_names

def search_by_name(filename: str, word: str):
    found_recipes = []
    recipes, recipes_names = copy_recipes(filename)
    for name in recipes_names:
        if name.upper().find(word.upper()) != -1:
            found_recipes.append(name)
    return found_recipes

def search_by_time(filename: str, prep_time: int):
    found_recipes = []
    recipes, recipes_names = copy_recipes(filename)
    for name in recipes_names:
        if recipes[name][0] <= prep_time:
            found_recipes.append(f"{name}, preparation time {recipes[name][0]} min")
    return found_recipes

def search_by_ingredient(filename: str, ingredient: str):
    found_recipes = []
    recipes, recipes_names = copy_recipes(filename)
    for name in recipes_names:
        for item in recipes[name][1]:
            if item.upper().find(ingredient.upper()) != -1:
                found_recipes.append(f"{name}, preparation time {recipes[name][0]} min")
    return found_recipes

# test
if __name__ == "__main__":
    # test 1
    # found_recipes = search_by_name("recipes1.txt", "cake")
    # for recipe in found_recipes:
    #     print(recipe)

    # test 2
    # found_recipes = search_by_time("recipes1.txt", 20)
    # for recipe in found_recipes:
    #     print(recipe)

    # test 3
    found_recipes = search_by_ingredient("recipes1.txt", "eggs")
    for recipe in found_recipes:
        print(recipe)