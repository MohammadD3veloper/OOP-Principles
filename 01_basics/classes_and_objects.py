""" Basic example of Class and Object in Python """


class Car:
    """ A Simple Car class """
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        """ Instance method """
        return f"{self.brand} {self.model} is driving ..."


# Usage
if __name__ == "__main__":
    car1 = Car("Tesla", "Model S")
    car2 = Car("BMW", "i8")

    print(car1.drive())
    print(car2.drive())
