hourWage = float(input("Hourly wage: "))
hoursWorked = float(input("Hours worked: "))
weekDay = input("Day of the week: ")

dailyWages = hourWage * hoursWorked

if weekDay == "Sunday":
    dailyWages = dailyWages * 2

print(f"Daily wages: {dailyWages} euros")