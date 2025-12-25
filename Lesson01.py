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
from fontTools.subset.svg import xpath
from sqlalchemy.util import ellipses_string

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

st = "1 Hello, world. Version 3 of Python is more powerful, than 2."
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

st = "Hello world. What a beautiful day is today"
# print(len(st.split()))
# ls = []
# for i in st:
#     if i not in " ":
#         ls.append(i)
# print(ls)

# list comprehension

# print([i for i in st if i not in " "])

st = "Hello, world!!! Today is 24.12.2025."

print([i for i in st if not i.isdigit() and i not in (" ", ".", ",", "!")])