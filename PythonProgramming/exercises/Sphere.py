from math import pi


class Sphere:

    def __init__(self, diameter):
        self.diameter = diameter


inputDiameter = float(input("The diameter of the sphere: "))
sphere = Sphere(inputDiameter)
volume = 4.0 / 3.0 * pi * (sphere.diameter / 2) ** 3
print("Volume of the cell = %f m" % round(volume, 6))
