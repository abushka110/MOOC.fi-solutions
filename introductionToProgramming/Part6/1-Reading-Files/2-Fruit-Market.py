# solution
def read_fruits():
    fruit_name_and_cost = {}
    with open("fruits.csv") as fruits_file:
        for line in fruits_file:
            fruit_and_cost = line.split(";")
            fruit_name_and_cost[fruit_and_cost[0]] = float(fruit_and_cost[1])
    return fruit_name_and_cost
    
read_fruits()