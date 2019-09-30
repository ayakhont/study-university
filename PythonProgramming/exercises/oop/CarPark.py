from typing import List
from Car import Car


class CarParking:

    cars: List[Car]

    def __init__(self, number_of_cars: int):
        self.cars = list()
        for i in range(0, number_of_cars):
            self.cars.append(Car("automate"))


if __name__ == "__main__":
    carParking = CarParking(10)
    print(carParking)