""" Difference between instance and class variable """


class Dog:
    species = "Canine"

    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == "__main__":
    d1 = Dog("Rex", 5)
    d2 = Dog("Buddy", 3)

    # instance variables, not accessible without creating an instance
    # (its not shared between all instance, each instance can see its own variable)
    print(d2.name)
    print(d1.name)

    print(Dog.species) # class variable, accessible without creating an instance
    Dog.species = "Mammal" # can modify without creating an instance
    print(d1.species) # a class variable is shared between all instance
    print(d2.species)
