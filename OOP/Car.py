from OOP.GearBox import GearBox


class Car():

    # field declaration
    ability: str
    # field initialization
    number_of_wheels = 4
    # declaration of gear_box
    gear_box: GearBox

    # constructor of Car class
    def __init__(self, name):
        # field initialization
        self.ability = name
        self.gear_box = GearBox(4)

    # polymorphic method in the context of its implementation in child and parent classes
    def present(self):
        print(self.ability)

    # example of encapsulation
    # We try to avoid direct access to field changing from outside the class like car.ability = "smth"
    # by using special methods for changing fields of class through these methods.
    # It is also can be useful to control the "state" of the object of this class (for example
    # we don't want to have only two state of our car:
    #  - initial: the values of fields are initialised while the object as Car was created
    #  - changed: the values of fields are changed only by method change_car())
    def change_car(self):
        self.ability = "ride has been changed"
        self.number_of_wheels = 3

    @staticmethod
    def print_idea():
        print("bikes sucks")


