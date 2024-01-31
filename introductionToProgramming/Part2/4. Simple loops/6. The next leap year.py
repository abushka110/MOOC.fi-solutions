year = int(input("Year: "))

yearLeap = year + 1

while True:
    if (yearLeap % 4 == 0 and yearLeap % 100 != 0) or (yearLeap % 400 == 0):
        break
    else:
        yearLeap += 1

print(f"The next leap year after {year} is {yearLeap}")