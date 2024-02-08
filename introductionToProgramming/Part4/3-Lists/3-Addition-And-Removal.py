list = []
print(f"The list is now {list}")

action = input("a(d)d, (r)emove or e(x)it: ")
value = 1

while action != "x":
    if action == "d":
        list.append(value)
        value += 1
    elif len(list) > 0 and action == "r":
        value -= 1
        list.remove(value)
    print(f"The list is now {list}")
    action = input("a(d)d, (r)emove or e(x)it: ")
        
print("Bye!")