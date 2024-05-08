# solution
class Item:
    def __init__(self, item_name: str, item_weight: int):
        self.item_name = item_name
        self.item_weight = item_weight

    def __str__(self) -> str:
        return f"{self.item_name} ({self.item_weight} kg)"
    
    def name(self) -> str:
        return self.item_name
    
    def weight(self) -> int:
        return self.item_weight
    
class Suitcase:
    def __init__(self, max_weight):
        self.maximum_weight = max_weight
        self.__current_weight = 0
        self.__items_in_case = []

    def __str__(self) -> str:
        if len(self.__items_in_case) == 1:
            return f"{len(self.__items_in_case)} item ({self.__current_weight} kg)"
        else:
            return f"{len(self.__items_in_case)} items ({self.__current_weight} kg)"

    def add_item(self, item):
        if self.__current_weight + item.weight() <= self.maximum_weight:
            self.__current_weight += item.weight()
            self.__items_in_case.append(item)

    def print_items(self):
        for item in self.__items_in_case:
            print(item)

    def weight(self):
        return self.__current_weight

# test
if __name__ == "__main__":
    # test 1
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)

    # print("Name of the book:", book.name())
    # print("Weight of the book:", book.weight())

    # print("Book:", book)
    # print("Phone:", phone)


    # test 2
    # book = Item("ABC Book", 2)
    # phone = Item("Nokia 3210", 1)
    # brick = Item("Brick", 4)

    # suitcase = Suitcase(5)
    # print(suitcase)

    # suitcase.add_item(book)
    # print(suitcase)

    # suitcase.add_item(phone)
    # print(suitcase)

    # suitcase.add_item(brick)
    # print(suitcase)


    # test 3
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)
    brick = Item("Brick", 4)

    suitcase = Suitcase(10)
    suitcase.add_item(book)
    suitcase.add_item(phone)
    suitcase.add_item(brick)

    print("The suitcase contains the following items:")
    suitcase.print_items()
    combined_weight = suitcase.weight()
    print(f"Combined weight: {combined_weight} kg")