print("Please type in integer numbers. Type in 0 to finish.")

# initialize number Count, Sum, positives and negatives count
num = 0
numsCount = 0
numsSum = 0
numsNegativesCount = 0
numsPositivesCount = 0

# ask for a number till there is no zero
while num != 0:
    numsCount += 1
    numsSum += num
    if num < 0:
        numsNegativesCount += 1
    else:
        numsPositivesCount += 1
    num = int(input("Number: "))

numsMean = float(numsSum) / float(numsCount)

print(f"Numbers typed in {numsCount}")
print(f"The sum of the numbers is {numsSum}")
print(f"The mean of the numbers is {numsMean}")
print(f"Positive numbers {numsPositivesCount}")
print(f"Negative numbers {numsNegativesCount}")