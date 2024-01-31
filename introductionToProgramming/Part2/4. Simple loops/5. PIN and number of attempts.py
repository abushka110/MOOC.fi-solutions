pin = 4321

pinTry = int(input("PIN: "))
numOfAttempts = 1

while pin != pinTry:
    print("Wrong")
    pinTry = int(input("PIN: "))
    numOfAttempts += 1

if numOfAttempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {numOfAttempts} attempts")