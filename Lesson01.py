# x = 5   # integer is immutable
# print(x)
# print(id(x))
# print(id(5))
# x = "Alexander" # string is immutable
# print(x)
# print(id(x))
# print(id(5))
# print(id("Alexander"))
# y = 4.12 # float is immutable
# x += 5  # x = x + 5
# print(id(x))
# z = "Sergey"
# print(id(z))
# v = z
# print(id(v))
# print(type(y))
# z = z + x
# z = 3 * z
# print(z)
# a = "a"
# a = 50 * a
# print(a)
# print(dir(z))


# txt = "Hello, group QA2048!"
# x = txt.upper()
# print(txt)
# print(txt.upper())
# print(txt.lower())
# print(txt.title())
# print(txt.capitalize())
# print(txt.replace("Hello", "Good bye"))
# x = "Hello"
# y = "Hello"
# print(x is y)
# print(id(x))
# print(id(y))

# name = input("Enter your name: ")
# age = input("Enter your age: ")
# print("Hello,", name + ". Next year you will be", age+1, ".")

# print(f"Hello, {name}. Next year you will be {int(age)+1}.")
# price = 34.99785
# x = input("Enter first number: ") # 5
# y = input("Enter second number: ") # 7
# z = int(x) + int(y)
# print(z)
# z = 2/3
# print(z)
# print(f"{z:.2f}")


# price = int(input("Enter the price: "))

# if price > 50:
#     print("It is so expensive")
# elif price > 40:
#     print("The price is OK")
# else:
#     print("The price is low")

# print("It is so expensive") if price > 50 else print("The price is low") if price <= 40 else print("The price is OK")

# print(f"The price is {'so high' if price > 50 else 'so low' if price <= 40 else 'OK'}")

# st = "Hello, world. How are you?"
# st2 = """   Hello, my friend.
# I want to say you about something fun
#         This is my mail with
#             many rows and indents"""
# print(print)
# print()
# print(len(st))
# # print(st[::3])
# print(st[::-1])

# x = 1
# while x<= 10:
#     print(x)
#     x += 2

# for x in range(10,0,-1):
#     print(x)

# st = "1 Hello, world. Version 3 of Python is more powerful, than 2."
# for l in st:
#     print(l, end="*")
# print(st)

# isalpha
# isdigit
# for l in st:
#     if l.isdigit():
#         print(l)

# for i in range(len(st)):
#     if st[i].isdigit():
#         print(f"digit {st[i]} is the {i+1} element")

# print(st.lower().count("h"))
# x = 2_000_000_000
# print(x)


# List - mutable, iterable, ordered, duplication enabled

# lst = [2, 4, 8 ,4, -5, 6 ,4, 8, 101, 4, 6, 7]
# lst2 = [2, 4, 8 ,4, -5]
# lst3 = lst
# lst5 = list(lst)
# print(lst == lst2)
# print(id(lst))
# print(id(lst2))
# print(id(lst3))
# lst2[-1] = 50
# print(lst2)
# lst[0] = 20
# print(lst3)
#
# print(lst5)
# print(id(lst5))

# boolean True False

# ls = [2, 5, "2", "hello", [5, -2], 3.14, True]
# print(ls)
# # print(ls[4::-1])
# print(ls[4][1])

# fruits = ["apple", "cherry", "banana"]
# print(fruits)

# for f in fruits:
#     print(f)
#
# print("banana" in fruits)

# if "banana" in fruits:
#     print(True)

# fruits[1:2] = ["orange", "cherry"]
# print(fruits)
#
# fruits[1:3] = ["melon"]
# print(fruits)

# fruits.append("orange")
# print(fruits)
# fruits.insert(1, "melon")
# print(fruits)
# tropical = ["guava", "pineapple", "mango"]
# tropical.extend(fruits)
# fruits.extend(tropical)
# lst5 = [1, "hello", True]
# new_fr = fruits + tropical + lst5
# print(new_fr)
# print(id(new_fr))
# cp_new_fr = new_fr.copy()
# print(cp_new_fr)
# print(id(cp_new_fr))
# print(new_fr == cp_new_fr)
# print(new_fr is cp_new_fr)
# n_fr_cp2 = fruits[::]
# print(n_fr_cp2 == fruits)
# print(n_fr_cp2 is fruits)

# st = "Hello world. What a beautiful day is today"
# print(len(st.split()))
# ls = []
# for i in st:
#     if i not in " ":
#         ls.append(i)
# print(ls)

# list comprehension

# print([i for i in st if i not in " "])

# st = "Hello, world!!! Today is 24.12.2025."
# list comprehension
# print([i for i in st if not i.isdigit() and i not in (" ", ".", ",", "!")])

# 5X5 *
# for i in range(5):
#     for j in range(7):
#         print('*', end=' ')
#     print()

# num = int(input("Enter some number: "))
# if num > 0:
#     print("positive")
# else:
#     print("not positive")
# short hand if operator
# print("positive") if num > 0 else print("negative") if num < 0 else print("Zero")

# st = "Hello, world!"
# for i in st:
#     print(i, end=":")
# short hand for with if
# [print(i, end=":") for i in st if i not in " "]

# st = "Hello, world!"
# for i in st:
#     if i == " ":
#         # continue - ignores all following rows inside for operator and goes toward the next element
#         break # breaks for loop and exits
#     print(i, end=":")

# print([i for i in range(1, 101) if i%2 == 0])
#
# print([i**2 for i in range(1, 101) if i%2 == 0])
#
# print([float(f"{i**0.5:.2f}") for i in range(1, 101) if i%2 == 0])

# txt = "Hello guys. We are learning python now. This is the great programming language"
# lst2 = [146, 318904834]
# lst2.append(['John', 'Smith', 'qa engineer'])
# lst = [145, 321903843]
# lst.append([w for w in txt.split() if len(w) > 5])
# #
# #
# # print(lst)
# workers = []
# workers.append(lst)
# workers.append(lst)
# print(workers)

# fruits = ["apple", "chery", "banana",  "watermelon", "Kiwi", "cherry"]
# fruits.remove("banana")
# print(fruits)
# print(fruits.pop())
# print(fruits)
# fruits.clear()
# del fruits
# print(fruits)

# print(fruits.count("cherry"))

# print(fruits[::-1])
# print(fruits)
# fruits.reverse()
# print(fruits)
# fruits.sort()
# sorted_fruits = sorted(fruits, reverse=True, key=len)
# print(fruits)
# print(sorted_fruits)

# x = 8
# y = 10
# z = y
# y = x
# x = z
# swapping
# x, y = y, x

# x, y = 8, 10

# creating sorted list from two sorted sub-lists

# lst1 = [1, 2, 3, 5, 7, 34, 99]
# lst2 = [2, 4, 6, 7, 23, 58, 67, 69]
#
# lst3 = []
# i, j = 0, 0
#
# while i < len(lst1) and j < len(lst2):
#     if lst1[i] < lst2[j]:
#         lst3.append(lst1[i])
#         i += 1
#         if i >= len(lst1):
#             while j < len(lst2):
#                 lst3.append(lst2[j])
#                 j += 1
#     else:
#         lst3.append(lst2[j])
#         j += 1
#         if j >= len(lst2):
#             while i < len(lst1):
#                 lst3.append(lst1[i])
#                 i += 1
#
# print(lst1)
# print(lst2)
# print(lst3)

# lst = [56, 13, 37, 5, 0, 37, -1, -4, -50]
# for i in range(len(lst) - 1):
#     for j in range(len(lst) - i - 1):
#         if lst[j] > lst[j+1]:
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(lst)

# function


# def hello():
#     print("Hello, world!")

# def hello(name, age):
#     print("Hello,", name, " you are", age)
#
#
# hello("Alexander", 25)
# hello("Sergey", 27)

# def max2(x, y):
#     if x > y:
#         return x
#     return y
#
# maximal = max2(400, 87)
# # print(maximal)
#
# def max3(x, y, z):
#     return max2(max2(x, y), z)
#
# print(max3(-5, -45, 2))

# def my_country(country="Israel", x = 10):
#     print("I'm from", country, "leave", x, "years")
#
# my_country("Sweden", 5)
# my_country()
# my_country("USA")

# def call_child(*kids): # (*args)
#     # print("My child's name is", kid)
#     if len(kids) > 0:
#         print("The youngest kid is", kids)
#
# call_child("Emile", "Mary", "Michael", "Jonny")

# def personal_info(*args, **kwargs):
#     k = len(args)
#     v = len(kwargs)
#     print(f"{args} these strings were passed to my function")
#     print(kwargs["age"])
#     return *args, k, v
#
# y = personal_info("John","Jack", "Hello world", surname="Conor", age=35, son="Jack", stam="kuku")
# print(y)
# y = 0
# def my_fun(x_copy):
#     # global y # not recommended
#     y = 5 * x_copy
#     x_copy = x_copy * 10
#     return y
#
# x = 5
# # y = (my_fun(x))
# print(y)
# print(x)

# factorial    6! 1*2*3*4*5*6
# num = 60
# def fact_not_rec(n):
#     fact = 1
#     for i in range(1,n+1):
#         fact *= i
#     return fact
#
# print(fact_not_rec(num))
#
# # recursion
#
# def fact_rec(n):
#     if n > 1:
#         return fact_rec(n-1) * n
#     return 1

# print(fact_rec(num))

# fibonacci
# i[n] = i[n-1] + i[n-2]
#
# import time
#
# num = 38
# lst = [1, 1]
# def fibo(x):
#     for i in range(2, x):
#         lst.append(lst[i-1] + lst[i-2])
# start = time.time()
# fibo(num)
# print(lst)
# print(f"Classic algorithm - {time.time() - start}")
# # 1, 1, 2, 3, 5, 8, 13, 21
# def fibo_rec(x):
#     if x > 1:
#         return fibo_rec(x-1) + fibo_rec(x-2)
#     return x
#
# def fib_list(n):
#     lst = []
#     for i in range(1,n+1):
#         lst.append(fibo_rec(i))
#     return lst
# start = time.time()
# print(fib_list(num))
# print(f"Recursive algorithm - {time.time() - start}")

# x = 5
# for i in range(100):   # O(n)
#     x += i
#
# x =5
# for j in range(100):
#     x += j
#
# for i in range(100):
#     for j in range(100):
#         for k in range(100): # O(n^3)
#             x += k
# print(x)

# Lambda functions - Anonymous functions

# def pr(st):
#     print(st)

# pr("Hello, world!")
# x = lambda : print("Hello, world!")
#
# x()
# x()

# print((lambda x: x*x)(8))

# lst = [5, 14, (lambda x: x*x)(14), "Hello"]
# print(lst)

# def get_filter(a, fil=None):
#     if not fil:
#         return a
#     return [y for y in a if fil(y)]
# lst = [1, 2, 4, 34, -4, -200, 45, 9]
# lst1 = get_filter(lst, lambda x: x >= 0)
# lst2 = get_filter(lst, lambda x: x%2 == 1)
# print(lst1)
# print(lst2)

# lst1 = [2, 5, -2]
# lst2 = [3, 3, 4]
# lst3 = [0, -40, 0]
# # print(*map(pow, lst1, lst2))
# #
# print(*map(lambda x, y, z: x*y+z, lst1, lst2, lst3))

# print(*map(lambda x: x*2, lst1))



# lst = [x for x in range(50)]
# print(*filter(lambda z: z%3 == 0, lst))

# seq = "Hello world. The evening is wonderful"
# print(list(filter(lambda vowels: vowels in ['a', 'e', 'i', 'o', 'u', 'y'], seq)))

# Кортеж
# Tuple iterable, ordered, duplicates enabled, immutable

# tpl = tuple(("apple", "banana", 4, 3.5, 4, True, (3, 5, 7), [10, 32, [], (), (4, 6, 7), -4]))
# # tpl = (5, 4)
# print(type(tpl))
# # print(len(tpl))
# print(tpl[6][2])
# print(tpl[-1][-1])
# # tpl[3] = 5
# # tpl[6][2] = 3 - doesn't work because of immutability
# print(type(tpl[-1]))
# # tpl[-1].append(1000)
# print(tpl)
# print(tpl[7][-2])
# tpl[7][-2][1] = "Hello"
# print(tpl)

# lst = [1, 2, 4, 5, 6]
# tpl = tuple(lst)
# print(tpl)

# tpl = (1, 2, 4, 5, 6, 45, 78, 90, 5, 4, 4, "iyeit", True)
# lst = list(tpl)
# # print(lst)
# lst.append(10)
# tpl = tuple(lst)
# print(lst)
# print(tpl)
# print(tpl.count(4))
# print(tpl.index(90))
# print(tpl.__sizeof__())
# print(lst.__sizeof__())

# fruits = ("apple", "banana", "cherry", "strawberry", "watermelon")
# (green, *yellow, red) = fruits
# print(fruits)
# print(yellow)

# lst = [i**2 for i in range(1, 110000)]
# print(lst.__sizeof__())
# print(lst[1000])
# tpl = (i**2 for i in range(1, 110000))
# print(tpl.__sizeof__())
# print(tuple(tpl)[1000])

# tpl1 = ('a', 'b', 'c')
# tpl2 = (1, 2, 3)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# mult_tpl = tpl2 * 3
# print(mult_tpl)

# lst = [(4, 5), (2, 3), (6, 7), (2, 8)]
# print(lst)
# l = len(lst)
# # bubble sort
# for i in range(l):
#     for j in range(l - i - 1):
#         if (lst[j][0] + lst[j][1]) > (lst[j+1][0] + lst[j+1][1]):
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#
# print(lst)
# my_types = (int, str, list)
# y = [3]
# x = isinstance(y, my_types)
# print(x)

# set : changeable, not ordered, not duplicates enabled, cannot contain other changeable types

# set1 = {0, 3, "hello", 5, 5, 5, 5.0, "hello",True, False, (3, 4, 6),0,0,0,0,0,0,0, 0}
# set2 = set()
# print(len(set1))
# for i in set1:
#     print(i)

# print(1 in set1)
#
# lst = [5, -7, 10]
# print(lst[2])

# print(hash("hel"))

# fruits = {"apple", "orange", "banana", "cherry"}
# print(fruits)
# tropical = ("kiwi", "pineapple", "mango")
# fruits.add("apricot")
# print(fruits)
# fruits.update(tropical)
# # print(fruits)
# fruits.discard("banana")
# print(fruits)
# fruits.discard("banana")
# deleted = fruits.pop()
# print(deleted)
# print(fruits)
# fruits.clear()
# print(fruits)
# del fruits
# print(fruits) - object doesn't exist

# set1 = {'a', 'b', 'c', (1, 2, 3)}
# set2 = {1, 2, 3, 'a', 'c', (1, 2, 3)}
# set3 = {"John", "Elena"}
# myset = set1.union(set2, set3)
# myset = set1 | set2 | set3
# print(myset)
# set1 |= set2
# print(set1)
# int_set = set1.intersection(set2)
# int_set = set1 & set2
# print(int_set)
# set1.intersection_update(set2)
# set1 &= set2
# print(set1)
# set1 = {'a', 'b', 'c', (1, 2, 3)}
# set2 = {1, 2, 3, 'a', 'c', (1, 2, 3)}
# set3 = {"John", "Elena"}

# print(set2.difference(set1))
# set1.difference_update(set2)
# print(set1)
# set2 -= set1
# print(set2)
# print(set2.symmetric_difference(set1))
# set2.symmetric_difference_update(set1)
# print(set2)
# set2 ^= set1
# print(set2)

# set1 = {2, 4, 6, 3, 0}
# set2 = {2, 4, 6}
# print(set2.issubset(set1))
# print(set1.issuperset(set2))

# performance
import time
MAX_VALUE = 10_000_000
SEARCH_ITEM = 9_999_990

lst = [i**2 for i in range(MAX_VALUE)]
st = {i**2 for i in range(MAX_VALUE)}
# print(lst)
# print(st)

start = time.time_ns()
print(SEARCH_ITEM**2 in st)
print(f" Search in set = {time.time_ns() - start}")

start = time.time_ns()
print(SEARCH_ITEM**2 in lst)
print(f" Search in list = {time.time_ns() - start}")


