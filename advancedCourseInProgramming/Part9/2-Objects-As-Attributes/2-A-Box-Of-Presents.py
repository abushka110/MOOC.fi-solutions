# solution
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"Present: {self.name} ({self.weight} kg)"

class Box:
    def __init__(self):
        self.box_presents = []

    def add_present(self, present: Present):
        self.box_presents.append(present)

    def total_weight(self):
        x_weight = 0
        for present in self.box_presents:
            x_weight += present.weight
        return x_weight

# test
if __name__ == "__main__":
    # test 1
    # book = Present("ABC Book", 2)
    # print("The name of the present:", book.name)
    # print("The weight of the present:", book.weight)
    # print("Present:", book)
    # output:
    # The name of the present: ABC Book
    # The weight of the present: 2
    # Present: ABC Book (2 kg)

    # test 2
    book = Present("ABC Book", 2)
    box = Box()
    box.add_present(book)
    print(box.total_weight())
    cd = Present("Pink Floyd: Dark Side of the Moon", 1)
    box.add_present(cd)
    print(box.total_weight())
    # output:
    # 2
    # 3
    