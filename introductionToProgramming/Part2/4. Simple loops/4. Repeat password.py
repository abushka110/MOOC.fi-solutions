password = input("Password: ")
passwordRepeat = input("Repeat password: ")

while password != passwordRepeat:
    print("They do not match!")
    passwordRepeat = input("Repeat password: ")

print("User account created!")