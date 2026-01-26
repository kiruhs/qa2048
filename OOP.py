# class is mutable type of data
# class Point:
#     color = "red"
#     radius = 3
# P = Point
# print(callable(P))
# a = P()
# print(callable(a))
# print(a.radius)
# a.coord = (5, 10)
# print(a.coord)
# a.radius = 300
# print(P.coord) no coord attribute in class P (Point)
# print(Point)
# print(a)
# print(a.__dict__)
# print(P.__dict__)


# class Point:
#     color = "black"
#     def __init__(self, x, y, size):
#         self.x = x
#         self.y = y
#         self.size = size
#
#     def get_coord(self):
#         return self.x, self.y
#
#     def my_color(self):
#         return self.color
#
# p1 = Point(5, 8, 2)
# print(p1.__dict__)
# # print(Point.__dict__)
# print(p1.color)
# p2 = Point(0, -3, 1)
# print(p2.__dict__)
#
# print(p2.get_coord())

# class Dog:
#     species = ("Canis faimiliaris")
#     __doc__ = "This type of objects describes properties and activities of dogs"
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def description(self):
#         return f"{self.name} is {self.age} years old"
#
#     def speak(self, sound):
#         return f"{self.name} says {sound}"
#
#     def __str__(self):
#         return f"Is is the dog with name {self.name}"
#
#
# d1 = Dog("Sharik", 4)
# print(d1.description())
# d2 = Dog("Tuzik", 3)
# print(d2.description())
# print(d2.speak("Wouf"))
# print(d1.speak("Woooo"))
#
# # help(d1)
# print(d1)
# print(d2)
#
# print(dir(Dog))
# print()
# print(dir(object))

# class Figure:
#     color = "black"
#     size = 2
#
# class Line(Figure):
#     length = 55
#
#     def draw(self):
#         print("Drawing the line")
#
# l1 = Line()
# # l1.color = "blue"
# print(l1.color)
# print(Line.__dict__)
# print(l1.__dict__)

# l1.draw()
# print(l1.length)
#
# Line.draw(l1)

# class Animal:
#     eyes = True
#     tail = True
#     blood = True
#
#     def eat(self):
#         return f"I have to it for growing"
#
#     def breath(self):
#         return "oxygen"


# class Fish(Animal):
#     fin = True
#     eyes = 2
#
#     def __init__(self, speed):
#         self.speed = speed
#
#     def swim(self):
#         print(f"swimming with {self.speed} kmph")


# class Beast(Animal):
#     legs = 4
#     head = 1
#     eyes = 2
#
#     def __init__(self, speed):
#         self.speed = speed
#
#     def run(self):
#         print(f"running with {self.speed} kmph")
#
# guppy = Fish(5)
# wolf = Beast(30)

# print(wolf.breath())
# print(guppy.breath())
# print(guppy.eyes)
# print(Animal.eyes)
# guppy.swim()
# wolf.run()

# print(isinstance(wolf, Fish))
# print(isinstance(wolf, Beast))
# print(isinstance(wolf, Animal))
# print(isinstance(wolf, object))

# Inheritance
lst = [1, 2, 4, 6]
# v = [1 2 4 6]
class Vector(list):
    # pass
    def __str__(self):
        return '['+" ".join(map(str, self))+']'

# v = Vector(lst)
# print(v)
# print(v[-1])
# v.append(15)
# print(v)

# print(lst.__class__)      <class 'list'>
# print(list.__class__)     <class 'type'>
# print(list.__bases__)     (<class 'object'>,)
# print(type.__class__)     <class 'type'>
# print(type.__bases__)     (<class 'object'>,)
# print(Vector.__bases__)   (<class 'list'>,)
# print(Vector.mro())       [<class '__main__.Vector'>, <class 'list'>, <class 'object'>]


# encapsulation - levels of safety/privacy

# class Point:
#     _color = "black"
#     def __init__(self, x=0, y=0):
#         self.__x = x
#         self.__y = y
#
#     @classmethod
#     def __check_value(cls, z):
#         return type(z) in (int, float)
#
#     def set_coord(self, x, y):
#         if self.__check_value(x) and self.__check_value(y):
#             self.__x = x  # private
#             self.__y = y  # private
#         else:
#             raise ValueError("The coordinates should be numbers")
#
#     def get_coord(self):
#         return self.__x, self.__y


# p = Point(4, 8)
# print(p.get_coord())
# try:
#     p.set_coord(55, 40)
#     print(p.get_coord())
# except ValueError as er:
#     print(er)

# print(dir(p))
# print(p._Point__x)
# p._Point__x = 100
# print(p._Point__x)
# print(p._color) # protected

# class Geom:
#     name = "Geom"
#     color = "blue"
#     line = 30
#     def draw(self):
#         print("Some figure drawing")
#
#     def get_per(self):
#         try:
#             raise NotImplementedError("This method should be implemented in a child class")
#         except (NotImplementedError, TypeError) as err:
#             print(err)
#
# g = Geom()
# # print(g.line)
# # print(g.name)
# # g.draw()
# # g.get_per()
#
# class Rect(Geom):
#
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h
#
#     def get_per(self):
#         return 2 * (self.w + self.h)
#
# class Square(Geom):
#     def __init__(self, l):
#         self.l = l
#
#     def get_per(self):
#         return 4 * self.l
#
# class Triangle(Geom):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def draw(self):
#         print("drawing triangle")
#
#     def get_per(self):
#         return self.a + self.b + self.c

# r1 = Rect(10, 5)
# print(r1.get_per())
# s1 = Square(12)
# print(s1.get_per())
# t1 = Triangle(5, 7, 11)
# print(t1.get_per())
# r1.draw()
# t1.draw()

# figures = [Rect(4, 7), Square(8), Square(11), Rect(12, 4), Triangle(6, 9, 9)]
#
# for f in figures:
#     print(f.get_per())

class Calculator:
    def add(self, a=0, b=0, c=0):
        print(a+b+c)

calc = Calculator()
calc.add(4, 8, 10)
calc.add(66)
calc.add(50, 80)
calc.add()