limit = int(input("Limit: "))

startNum = 1

numSum = startNum

while numSum < limit:
    startNum +=1
    numSum += startNum

print(numSum)