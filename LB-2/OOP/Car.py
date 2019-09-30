class Car:

    ability: str
    number_of_wheels = 4

    def __init__(self, name):
        self.ability = name

    def present(self):
        print(self.ability)

    def change_car(self):
        self.ability = "ride has been changed"
        self.number_of_wheels = 3

class Porsche(Car):

    cool_cabin: str

    def __init__(self):
        super().__init__("ride in cool way")
        self.cool_cabin = "realy cool cabin"

    def present(self):
        print(self.cool_cabin)