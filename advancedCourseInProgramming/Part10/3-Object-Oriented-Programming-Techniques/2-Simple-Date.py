# solution
class SimpleDate:
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, other):
        return (self.year, self.month, self.day) == (other.year, other.month, other.day)

    def __ne__(self, other):
        return (self.year, self.month, self.day) != (other.year, other.month, other.day)

    def __lt__(self, other):
        return (self.year, self.month, self.day) < (other.year, other.month, other.day)

    def __gt__(self, other):
        return (self.year, self.month, self.day) > (other.year, other.month, other.day)
    
    def __add__(self, days):
        day = self.day
        month = self.month
        year = self.year

        day += days
        while day > 30:
            day -= 30
            month += 1
            if month > 12:
                month = 1
                year += 1

        return SimpleDate(day, month, year)
    



# test
if __name__ == "__main__":
    # test 1
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = SimpleDate(28, 12, 1985)
    # print(d1)
    # print(d2)
    # print(d1 == d2)
    # print(d1 != d2)
    # print(d1 == d3)
    # print(d1 < d2)
    # print(d1 > d2)

    # test 2
    # d1 = SimpleDate(4, 10, 2020)
    # d2 = SimpleDate(28, 12, 1985)
    # d3 = d1 + 3
    # d4 = d2 + 400
    # print(d1)
    # print(d2)
    # print(d3)
    # print(d4)