# solution
from datetime import datetime

birth_day = int(input("Day: "))
birth_month = int(input("Month: "))
birth_year = int(input("Year: "))
birth = datetime(birth_year, birth_month, birth_day)
millennium = datetime(1999, 12, 31)
if birth < millennium:
    difference = millennium - birth
    print(f"You were {difference.days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
