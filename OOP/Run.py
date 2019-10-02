from OOP.Car import Car
import pickle
from OOP.Porsche import Porsche

if __name__ == "__main__":

    # creating the instance of Car class (or we can say creating the object of type Car)
    car = Car("ride")
    # calling the method of our object
    print("Below is representation of instance of Car:")
    car.present()
    print("The ability of our car: ", car.ability)

    # creating the instance of Porsche class (or we can say creating the object of type Porsche)
    another_car = Porsche()
    # printing the field of parent class from instance of child
    print("The ability of our Porsche car: ", another_car.ability)

    print("Below is representation of instance of Porsche:")
    another_car.present()

    # let's printing the fields of Car instance
    print("ability: ", car.ability)
    print("number_of_wheels: ", car.number_of_wheels)
    # let's change the values of our instance
    car.change_car()
    # let's printing the fields of Car instance again
    print("ability: ", car.ability)
    print("number_of_wheels: ", car.number_of_wheels)

    # below is example of serialisation and deserialization
    deserialized_car: Porsche
    with open("file", "wb") as file:
        pickle.dump(another_car, file)
    with open("file", "rb") as file:
        deserialized_car = pickle.load(file)

    deserialized_car.present()