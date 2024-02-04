num  = int(input("Please type in a number: "))

index = 1
index2 = num

while index <= num / 2:
    print(index)
    print(index2)
    index += 1
    index2 -= 1

if num % 2 != 0:
    print(index)