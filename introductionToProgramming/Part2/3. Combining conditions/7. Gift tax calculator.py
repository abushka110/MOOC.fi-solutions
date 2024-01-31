giftsValue = float(input("Value of gift: "))

tax = 0.0

if giftsValue >= 5000 and giftsValue < 25000:
    tax = (giftsValue - 5000) * 0.08 + 100
elif giftsValue >= 25000 and giftsValue < 55000:
    tax = (giftsValue - 25000) * 0.10 + 1700
elif giftsValue >= 55000 and giftsValue < 200000:
    tax = (giftsValue - 55000) * 0.12 + 4700
elif giftsValue >= 200000 and giftsValue < 1000000:
    tax = (giftsValue - 200000) * 0.15 + 22100
elif giftsValue >= 1000000:
    tax = (giftsValue - 1000000) * 0.17 + 142100

if tax == 0.0:
    print("No tax!")
else:
    print(f"Amount of tax: {tax} euros")