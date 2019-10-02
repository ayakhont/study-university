from OOP.Car import Car


# Porsche class inherited from Car class
# or we can say that Car class is a parent class for Porsche
# or Porsche class extends Car class
class Porsche(Car):

    # field declaration
    # the field of Porsche class only
    cool_cabin: str

    # constructor of Porsche class
    def __init__(self):
        # we initialise the constructor of parent class
        super().__init__("ride in cool way")
        self.cool_cabin = "really cool cabin"

    # polymorphic method in the context of its implementation in child and parent classes
    def present(self):
        print(self.cool_cabin)