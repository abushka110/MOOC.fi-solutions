lunchTimes = input("How many times a week do you eat at the student cafeteria? ")
lunchCost = input("The price of a typical student lunch? ")
groceries = input("How much money do you spend on groceries in a week? ")

weekly = float(groceries) + (float(lunchTimes) * float(lunchCost))
daily = weekly / 7.0
print("Average food expenditure:")
print("Daily:", daily, "euros")
print("Weekly:", weekly, "euros")