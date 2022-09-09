from abc import ABC, abstractmethod


class FormaGeometrica(ABC):
    PI = 3.14

    @abstractmethod
    def area(self):
        raise NotImplementedError('Metoda nu este implementata')

    @staticmethod
    def describe(self):
        print('Cel mai probabil am colturi')


class Patrat(FormaGeometrica):

    def __init__(self, latura):
        self.__latura = latura

    def area(self):
        return self.__latura ** 2

    def describe(self):
        print('Am colturi')

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Getter: latura este: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Setter: Noua latura este: {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Deleter: Am sters latura')
        self.__latura = None


class Cerc(FormaGeometrica):

    def __init__(self, raza):
        self.__raza = raza

    def area(self):
        return self.PI*(self.__raza*2)

    def describe(self):
        print('Eu nu am colturi')

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Getter: Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Setter: Noua raza este {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Deleter: Am sters raza')
        self.__raza = None


cerc1 = Cerc(raza=3)
cerc1.describe()
print(f'Aria cercului este: {cerc1.area()}')
cerc1.raza
cerc1.raza = 2
del cerc1.raza
patrat1 = Patrat(latura=4)
patrat1.describe()
print(f'Aria patratului este: {patrat1.area()}')
patrat1.latura
patrat1.latura = 3
del patrat1.latura

# Method Overloading:
# Method Overloading is an example of Compile time polymorphism.
# In this, more than one method of the same class shares the same method name having different signatures.
# Method overloading is used to add more to the behavior of methods and there is no need of more than one class
# for method overloading.
# Note: Python does not support method overloading.
# We may overload the methods but can only use the latest defined method.
# if datatype is int
# initialize answer as 0
# if datatype == 'int':
#     answer = 0
#
# # if datatype is str
# # initialize answer as ''
# if datatype == 'str':
#     answer = ''
#
# # Traverse through the arguments
# for x in args:
#     # This will do addition if the
#     # arguments are int. Or concatenation
#     # if the arguments are str
#     answer = answer + x
#
# print(answer)
#
# # Integer
# add('int', 5, 6)
#
# # String
# add('str', 'Hi ', 'Geeks')
# Method Overriding:
# Method overriding is an example of run time polymorphism.
# In this, the specific implementation of the method that is already provided by the parent class
# is provided by the child class.
# It is used to change the behavior of existing methods and there is a need for at least two classes
# for method overriding. In method overriding, inheritance always required as it is done
# between parent class(superclass) and child class(child class) methods.
