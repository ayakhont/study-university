from typing import List

from OOP.Car import Car
from OOP.Porsche import Porsche


class ParkingPlace:

    number_of_cars: int
    set_of_cars: List[Car]
    porsche_place: Porsche

    def __init__(self, number_of_cars):
        self.number_of_cars = number_of_cars
        self.set_of_cars = list()

    def park_car(self, car: Car, additional_wheel=2) -> str:
        self.set_of_cars.append(car)
        print(additional_wheel)
        string = "success"
        return string

if __name__ == "__main__":
    porsche = Porsche()
    car = Car("drive drunk")
    parkingPlace = ParkingPlace(10)
    parkingPlace.park_car(car, 4)

