from OOP.Car import Car, Porsche
import pickle

if __name__ == "__main__":

    car = Car("ride")
    car.present()
    print(car.ability)

    another_car = Porsche()
    print(another_car.ability)
    another_car.present()

    car.ability = "123"
    print(car.ability)

    desirialized_car: Porsche
    with open("file", "wb") as file:
        pickle.dump(another_car, file)
    with open("file", "rb") as file:
        desirialized_car = pickle.load(file)

    desirialized_car.present()