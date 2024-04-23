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

stats = NumberStats()
ask_num = int(input("Please type in integer numbers:\n"))
while ask_num != -1:
    stats.add_number(ask_num)
    ask_num = int(input(""))

print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")