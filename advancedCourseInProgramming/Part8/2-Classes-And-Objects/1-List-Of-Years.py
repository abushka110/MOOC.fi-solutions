# solution
from datetime import date

def list_years(dates: list):
    years_sorted = []
    for date_x in sorted(dates):
        years_sorted.append(date_x.year)
    return years_sorted

# test
if __name__ == "__main__":
    date1 = date(2019, 2, 3)
    date2 = date(2006, 10, 10)
    date3 = date(1993, 5, 9)

    years = list_years([date1, date2, date3])
    print(years)
    # Sample output
    # [1993, 2006, 2019]
