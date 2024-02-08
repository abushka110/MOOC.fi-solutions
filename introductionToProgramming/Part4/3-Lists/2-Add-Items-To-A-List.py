itemCount = int(input("How many items: "))
index = 1
numbers = []

while index <= itemCount:
    numbers.append(int(input(f"Item {index}: ")))
    index += 1

print(numbers)