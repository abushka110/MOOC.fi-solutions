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

# test
if __name__ == "__main__":
    # test 1
    book = Item("ABC Book", 2)
    phone = Item("Nokia 3210", 1)

    print("Name of the book:", book.name())
    print("Weight of the book:", book.weight())

    print("Book:", book)
    print("Phone:", phone)