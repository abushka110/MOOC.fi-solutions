# solution
class Car:
    def __init__(self) -> None:
        self.__petrol_in_tank = 0
        self.__odometer_km = 0
    
    def fill_up(self):
        self.__petrol_in_tank = 60

    def drive(self, km:int):
        if self.__petrol_in_tank >= km:
            self.__odometer_km += km
            self.__petrol_in_tank -= km
        else:
            self.__odometer_km += self.__petrol_in_tank 
            self.__petrol_in_tank -= self.__petrol_in_tank 
    
    def __str__(self) -> str:
        return f"Car: odometer reading {self.__odometer_km} km, petrol remaining {self.__petrol_in_tank} litres"

# test
if __name__ == "__main__":
    car = Car()
    print(car)
    car.fill_up()
    print(car)
    car.drive(20)
    print(car)
    car.drive(50)
    print(car)
    car.drive(10)
    print(car)
    car.fill_up()
    car.fill_up()
    print(car)