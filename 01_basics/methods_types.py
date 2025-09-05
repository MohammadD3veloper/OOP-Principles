""" Instance, Classmethod, StaticMethod Implementation """


class MathOps:
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        """ Can access instance attributes """
        return f"Instance method: value = {self.value}"

    @classmethod
    def class_method(cls):
        """ Can access class itself, not instance """
        return f"Class Method: called on  {cls.__name__}"

    @staticmethod
    def static_method(x, y):
        """ Utility method, independent of instance/class """
        return f"Static method result: = {x + y}"


if __name__ == "__main__":
    obj = MathOps(10)
    print(obj.instance_method()) # can't call without instance
    print(obj.class_method()) # can call by instance
    print(MathOps.class_method()) # can call without instance
    print(obj.static_method(5, 6)) # can call by instance
    print(MathOps.static_method(5, 6)) # can call without instance
