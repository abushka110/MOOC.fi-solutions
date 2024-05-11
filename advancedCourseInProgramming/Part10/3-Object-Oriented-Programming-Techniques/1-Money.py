# solution
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if self.__cents < 10:
            return f"{self.__euros}.0{self.__cents} eur"
        else:
            return f"{self.__euros}.{self.__cents} eur"
        
    def __sum(self):
        if self.__cents < 10:
            return float(f"{self.__euros}.0{self.__cents}")
        else:
            return float(f"{self.__euros}.{self.__cents}")
        
    def __eq__(self, another):
        return self.__sum() == another.__sum()
    
    def __lt__(self, another):
        return self.__sum() < another.__sum()
        
    def __gt__(self, another):
        return self.__sum() > another.__sum()
        
    def __ne__(self, another):
        return self.__sum() != another.__sum()
        
    def __add__(self, another):
        sum = self.__sum() + another.__sum()
        sum = round(sum, 2)
        if sum > 0:
            dollars = int(sum)
            cents = round((sum % 1) * 100)
            return Money(dollars, cents)
        else:
            raise ValueError("a negative result is not allowed")
        
    def __sub__ (self, another):
        sum = self.__sum() - another.__sum()
        sum = round(sum, 2)
        if sum > 0:
            dollars = int(sum)
            cents = round((sum % 1) * 100)
            return Money(dollars, cents)
        else:
            raise ValueError("a negative result is not allowed")

# test
if __name__ == "__main__":
    # test 1
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # e3 = Money(4, 10)
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e2)
    # print(e1 == e3)
    # # expected output:
    # # 4.10 eur
    # # 2.05 eur
    # # 4.10 eur
    # # False
    # # True

    # # test 2
    # e1 = Money(4, 10)
    # e2 = Money(2, 5)
    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)
    # # expected output:
    # # True
    # # False
    # # True

    # test 3
    e1 = Money(4, 5)
    e2 = Money(2, 95)
    e3 = e1 + e2
    e4 = e1 - e2
    print(e3)
    print(e4)
    e5 = e2-e1
    # expected output:
    # 7.00 eur
    # 1.10 eur
    # Traceback (most recent call last):
    # File "money.py", line 416, in 
    # e5 = e2-e1
    # File "money.py", line 404, in sub
    # raise ValueError(f"a negative result is not allowed")
    # ValueError: a negative result is not allowed