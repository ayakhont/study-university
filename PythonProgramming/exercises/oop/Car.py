from wsgiref.validate import validator


class Car:

    ability: str
    gearbox: str

    def __init__(self, gearbox="manual"):
        self.ability = "ride"
        self.gearbox = gearbox

    def present(self):
        print("I'm a common stupid car. I can ", self.ability)

    def wonder_me(self):
        print("I have 4 wheels")

    def get_gearbox(self) -> str:
        return self.ability

    def set_gearbox(self, gearbox: str):
        self.gearbox = gearbox



class Cabriolet(Car):

    roof_exists: bool

    def __init__(self):
        self.roof = True
        super().__init__()

    def present(self):
        print("My roof is on fire. I also can ", self.ability)

    def remove_the_roof(self) -> None:
        self.roof_exists = False
        print("The roof disappeared: ", not self.roof_exists)


if __name__ == "__main__":
    some_car = Car()
    some_car.present()

    special_car = Cabriolet()
    special_car.present()
    special_car.wonder_me()
    special_car.remove_the_roof()
    print(special_car.get_gearbox())