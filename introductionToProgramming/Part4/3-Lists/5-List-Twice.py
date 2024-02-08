list = []
itemNew = int(input("New item: "))

while itemNew != 0:
    list.append(itemNew)
    print(f"The list now: {list}" )
    print(f"The list in order: {sorted(list)}")
    itemNew = int(input("New item: "))

print("Bye!")