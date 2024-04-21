# solution
def smallest_average(person1: dict, person2: dict, person3: dict):
    ave1 = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
    ave2 = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
    ave3 = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

    if ave1 < ave2 and ave1 < ave3:
        return person1
    elif ave2 < ave1 and ave2 < ave3:
        return person2
    elif ave3 < ave1 and ave3 < ave2:
        return person3

# test
if __name__ == "__main__":
    person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
    person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
    person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

    print(smallest_average(person1, person2, person3))
    # {'name': 'Larry', 'result1': 3, 'result2': 1, 'result3': 1}