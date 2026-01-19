# from time import time, time_ns
# print(dir(time))
# print(time())
# dictionary unpacking
from fontTools.misc.cython import returns

import my_functions

# def my_fish(guppies, zebras, bettas):
#     print(f"I have {guppies} guppies fish")
#     print(f"I have {zebras} zebras fish")
#     print(f"I have {bettas} bettas fish")

# aquarium = {"guppies": 3,
#             "zebras": 5,
#             "bettas": 8,
#             "golden fish": 4,
#             "tuna": 2,
#             "salmon": 6}
#
# my_functions.my_fish(**aquarium)

# errors handling
# while True:
#     try:
#         x = int(input("Enter a number: "))
#         print(x+5)
#         break
#     except ValueError:
#         print("Oops! That wasn't valid number. Try again... ")
#
# print("The program runs forward")

# try:
#     f = open("test5.txt")
# except FileNotFoundError:
#     print("Try another file, no such one")

# try:
#     print(x)
# except NameError as err:
#     print(err)

# def division(x, y):
#     try:
#         res = x/y
#         print(f"result is {res}")
#     except Exception as z:
#         print(z)
#     # except TypeError as t:
#     #     print(t)
#
# division(4, 2)
# division(5, 0)
# division('n', 'r')

# x = int(input("Enter the temperature value between 20 and 50 degrees: "))
# try:
#     try:
#         x = int(input("Enter the temperature value between 20 and 50 degrees: "))
#     except ValueError as er:
#         print(er)
#         exit(0)
#     else:
#         if x < 20 or x > 50:
#             raise ValueError("You have entered invalid temperature value")
#         print("Good guy. You entered the valid temperature")
# except ValueError as e:
#     print(e)

# def sum_list(l):
#     x = 0
#     for i in l:
#         x += i
#     return x
#
# x = input("Enter 5 numbers to operate: ")
# y = x.split()
# for j in range(len(y)):
#     y[j] = int(y[j])
# print(sum_list(y))

# KeyboardInterrupt
# words = {}
# try:
#     while True:
#         s = input("Enter a word: ")
#         if s in words:
#             print(f"Word {s} is translated to {words[s]}")
#         else:
#             print(f"type the translation to russian for {s} : ")
#             words[s] = input()
# except KeyboardInterrupt:
#     print("Good bye!")
#     print(words)


# def sum_list(l):
#     x = 0
#     try:
#         for i in l:
#             x += int(i)
#         return x
#     except ValueError as v:
#         print(v)
#         return 0
#     finally:
#         print("This message is sent anyway")
# x = input("Enter 5 numbers to operate: ")
# y = x.split()
# print(sum_list(y))

# class ValueIsTooSmall(Exception):
#     pass
#
# class ValueIsTooLarge(Exception):
#     pass


# x = int(input("Enter the temperature value between 20 and 50 degrees: "))
# try:
#     try:
#         x = int(input("Enter the temperature value between 20 and 50 degrees: "))
#     except ValueError as er:
#         print(er)
#         exit(0)
#     else:
#         if x < 20:
#             raise ValueIsTooSmall("You have entered so low temperature value")
#         elif x > 50:
#             raise ValueIsTooLarge("You have entered so high temperature value")
#         print("Good guy. You entered the valid temperature")
# except (ValueIsTooLarge, ValueIsTooSmall) as e:
#     print(e)

# Generators and iterators
# lst = [n for n in range(50)]
# print(lst)

# obj = map(int, [1, 2, 3, '5', '67', 5.0])
# print(obj)
# print(5 in obj)
# print(next(obj))
# for _ in range(3):
#     print(next(obj))
# print(2 in obj)
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# print(next(obj))
# l = list(obj)
# print(l)
# print(obj.__sizeof__())
# print(l.__sizeof__())

# print(dir(obj))
# print(dir(l))

# res = []
# def func(n):
#     cnt = 1
#     while cnt <= n:
#         res.append(cnt**2)
#         cnt += 1
#     return res
#
# func(100)
# print(res)

# n = 0
# def func_2():
#     global n
#     n += 1
#     yield n
# print(func_2())
# print(func_2())
# print(func_2())
# for i in range(500):
#     print(next(func_2()))
# print(next(func_2()))

"""
A dictionary contains List as a value. Write a Python program to clear the list values in the said dictionary.

Original Dictionary:
{'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}

Clear the list values in the said dictionary:
{'C1': [], 'C2': [], 'C3': []}

Write a Python program to get the depth of a dictionary.
Original Dictionary:
{'a': 1, 'b': {'c': {'d': {}}}}
=============
Write a  Python function find the length of the longest increasing sub-sequence in a list
Original list:
[10, 20, 30, 40, 50, 30, 30, 20, 21, 34, 56, 78, 89,90,100]
Length of the longest increasing sub-sequence in the said list:
8
"""