class car:
    id = 0
    name = ""  # class variable

    def prinval(self):
        print(self.id, self.name)

    def __init__(self, id, name, yearin):
        print("Constructor called")
        self.__var = ("__ here indicate variable is private and cannot be accessed directly but threr exist a indirect "
                      "way in python to access such variable")

        self.id = id
        self.name = name
        year = yearin  # instance variable

    # getter
    @property
    def value10(self):
        return self.name * 10

    @value10.setter  # IMPORTANT
    def value10(self, newvalue):
        self.name = newvalue

    @classmethod
    def classmethod(cls, name):  # cls here refers to class and cls is  used by convention
        print("class method called")
        cls.name = name
        """
        class method are methods used to bring changes to classes
        """

    @classmethod
    def from_string(cls, string):
        name, id = string.split(',')
        return cls(name, int(id))

    def __str__(self):  # __str__ is command used for this
        return f"The name is {self.name}"  # the returned string will be printed if someone print a class instance


class child(car):
    def child_method(self):
        print("This is the child method.")
        super().from_string()
        """
        super method is used when  parent method is to be called in a child class
        """
    def __init__(self):
        print("child constructor called")
        super().__init__(1, "audi")
        super().prinval()

    def prinval(self):
        print("child prinval called")

    @staticmethod
    # for static function you not need to add self as argument as they are just normal function placed
    # inside a class
    def test_fun():
        print("Hello")


obj = car()
obj2 = car(2, "Audi")
obj.id = 1
obj.name = "BMW"
print(obj.id, obj.name)
obj.prinval()

"""decorators"""


def greet(fx):
    def mfx(*args, **kwargs):  # important
        print("good morning")
        fx(*args, **kwargs)  # important
        print("good night")

    return mfx  # important


@greet
def fun1():
    print("hello world")


@greet
def fun2(name):
    print(f"Hi to {name}")


fun1()

fun2("sam")


class vector:
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k

    def __add__(self,
                other):  # here __add__ is defining what will happen when + operator is applied on the class instances
        return vector(self.i + other.i, self.i + other.j, self.k + other.k)

    def __str__(self):
        return f"{self.i}i+{self.j}j+{self.k}k"


v1 = vector(1, 2, 3)
v2 = vector(1, 2, 3)
print(v1 + v2)  # "+" operator is here acting the wat defined above using __add__ method
# and printing in the wat due to __str__ function
"""
this is called operator overriding 
using this we can define a certain action will occur when a particular operator is used
"""


"""single inheritance"""


class test:
    a = 1


class test1(test):
    b = 2


"""multiple inheritance"""

""" multiple inheritance refers that one child class have multiple parent class"""


class parent_class_1:
    a = 1


class parent_class_2:
    b = 2


class child_class(parent_class_2, parent_class_1):
    c = 1
