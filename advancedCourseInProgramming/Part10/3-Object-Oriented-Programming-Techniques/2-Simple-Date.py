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
    
    def __sub__(self, other):
        # if not isinstance(other, SimpleDate):
        #     raise TypeError("unsupported operand type(s) for -: 'SimpleDate' and " + str(type(other)))

        total_days_self = self.day + self.month * 30 + self.year * 360
        total_days_other = other.day + other.month * 30 + other.year * 360

        return abs(total_days_self - total_days_other)  
    
# model solution
# class SimpleDate:
#     def __init__(self, pv: int, month: int, year: int):
#         self.__pv = pv
#         self.__month = month
#         self.__year = year
 
#     def __str__(self):
#         return f'{self.__pv}.{self.__month}.{self.__year}'
 
#     # Comparisons are easier, when date is converted to days
#     def __value(self):
#         return self.__year * 360 + self.__month * 30 + self.__pv
 
#     # Converst days back to date
#     def __to_date(self, days: int):
#         months = days // 30
#         years = months // 12
#         days -= months * 30
#         months -= years * 12
#         return SimpleDate(days, months, years)
 
#     def __lt__(self, other: "SimpleDate"):
#         return self.__value() < other.__value()
 
#     def __gt__(self, other: "SimpleDate"):
#         return self.__value() > other.__value()
 
#     def __eq__(self, other: "SimpleDate"):
#         return self.__value() == other.__value()
        
#     def __ne__(self, other: "SimpleDate"):
#         return self.__value() != other.__value()
 
#     def __add__(self, days_to_add: int):
#         return self.__to_date(self.__value() + days_to_add)
 
#     def __sub__(self, other: "SimpleDate"):
#         # abs(x) returns the absolute value of x
#         return abs(self.__value() - other.__value())

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

    # test 3
    d1 = SimpleDate(4, 10, 2020)
    d2 = SimpleDate(2, 11, 2020)
    d3 = SimpleDate(28, 12, 1985)
    print(d2-d1)
    print(d1-d2)
    print(d1-d3)