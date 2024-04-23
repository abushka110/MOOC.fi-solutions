# solution
# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = []

    def add_number(self, number:int):
        self.numbers.append(number)

    def count_numbers(self):
        return(len(self.numbers))
    
    def get_sum(self):
        return sum(self.numbers)

    def average(self):
        if len(self.numbers) != 0:
            return sum(self.numbers) / len(self.numbers)
        else:
            return 0

# test
if __name__ == "__main__":
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
