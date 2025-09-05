""" Property, Getter, Setter Implementation """


class Person:
    def __init__(self, name, age):
        self.__name = name
        self._age = age

    @property
    def age(self):
        """ Property itself creates a getter
        dosent required to override it by age.getter
        if we dont want to personalize it"""
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative!")
        self._age = value

    @property
    def name(self):
        return self.__name

    @name.getter
    def name(self):
        return self.__name.upper()

    @name.setter
    def name(self, value):
        self.__name = value


# change variable using setter and getter
p = Person("Adam", 25)
print(p.age)
p.age = 10
print(p.age)

# Changing private variable using setter and getters
print(p.name)
p.name = "Sandy"
print(p.name)
