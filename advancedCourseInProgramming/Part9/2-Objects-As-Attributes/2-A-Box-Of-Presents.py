# solution
class Present:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight

    def __str__(self) -> str:
        return f"Present: {self.name} ({self.weight} kg)"

# test
if __name__ == "__main__":
    book = Present("ABC Book", 2)

    print("The name of the present:", book.name)
    print("The weight of the present:", book.weight)
    print("Present:", book)
    
    # The name of the present: ABC Book
    # The weight of the present: 2
    # Present: ABC Book (2 kg)