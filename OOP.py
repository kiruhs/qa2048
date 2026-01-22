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

class Animal:
    eyes = True
    tail = True
    blood = True

    def eat(self):
        return f"I have to it for growing"

    def breath(self):
        return "oxygen"


class Fish(Animal):
    fin = True
    eyes = 2

    def __init__(self, speed):
        self.speed = speed

    def swim(self):
        print(f"swimming with {self.speed} kmph")


class Beast(Animal):
    legs = 4
    head = 1
    eyes = 2

    def __init__(self, speed):
        self.speed = speed

    def run(self):
        print(f"running with {self.speed} kmph")

guppy = Fish(5)
wolf = Beast(30)

# print(wolf.breath())
# print(guppy.breath())
# print(guppy.eyes)
# print(Animal.eyes)
# guppy.swim()
# wolf.run()

print(isinstance(wolf, Fish))
print(isinstance(wolf, Beast))
print(isinstance(wolf, Animal))
print(isinstance(wolf, object))