limit = int(input("Limit: "))

startNum = 1

numSum = startNum

sumStr = "1"

while numSum < limit:
    startNum +=1
    numSum += startNum
    sumStr += f" + {startNum}"

print(f"The consecutive sum: {sumStr} = {numSum}")