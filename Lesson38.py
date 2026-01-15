# dictionary - iterable, not indexed, not ordered(?), pairs containing, key:value, keys not duplicated, mutable

# dct = {}
# dct2 = dict()
# dct = {"brand": "Ford",
#        "model": ["Mustang", "Focus", "Fiesta"],
#        "year": 1980,
#        "year": 2010}
# print(dct)
# print(len(dct))
# # print(dct["brand"])
# # print(dct.get("year"))
# dct["year"] = 2022
# # print(dct.get("year"))
# dct["color"] = ("red", "green", "blue")
# print(id(dct["color"]))
# dct["color"] = ("red", "green", "blue", "white", "black")
# print(id(dct["color"]))
# print(id(dct["model"]))
# dct["model"].append("Edge")
# print(dct)
# print(id(dct["model"]))

# new_dict = dict(name = "John", age = 65, weight = 65, country = "USA")
# print(new_dict)
# print(new_dict.keys())
# print(new_dict.values())
#
# print(new_dict.items())
# new_dict.update({"country": "Ireland"})
# print(new_dict)
# print(new_dict.popitem())
# print(new_dict)
# print(new_dict.pop("age"))
# print(new_dict)
# new_dict.clear()
# print(new_dict)

# for x in new_dict: # printing of all keys
#     print(x)
#
# for x in new_dict.keys(): # printing of all keys
#     print(x)

# for x in new_dict.values(): # printing of all values
#     print(x)
#
# for x in new_dict:
#     print(new_dict[x]) # printing of all values

# for key, value in new_dict.items():
#     print(key, value, sep=" - ")

# copy_dict = new_dict.copy()
# print(copy_dict)
# print(new_dict)
# sec_copy_dict = dict(new_dict)
# print(sec_copy_dict)

# if 45 in new_dict.values():
#     print("Ok")
#
# if "country" in new_dict.keys():
#     print("We have country")

# for k, v in new_dict.items():
#     if v == 65:
#         print(k)

# nested dictionaries
import pprint
from tokenize import Ignore


# dct = {(1, 2, 3): 5}
# print(dct)

# my_kids = {
#     "child1": {
#         "name": "Bob",
#         "dob": 2004
#     },
#     "child2": {
#         "name": "Alice",
#         "dob": 2011
#     },
#     "child3": {
#         "name": "John",
#         "dob": 2014,
#         "hobby": "painting"
#     }
# }
# # print(my_kids)
# pprint.pprint(my_kids)
#
# print(my_kids["child3"]["dob"])
# my_kids["child2"]["dob"] = 2012
# my_kids["child1"]["hobby"] = "singing"
# pprint.pprint(my_kids)

# child1 = {
#         "name": "Bob",
#         "dob": 2004
#     }
#
# child2 = {
#         "name": "Mary",
#         "dob": 2014,
#         "hobby": "running"
#     }
# my_kids = {"kid1": child1, "kid2": child2}
# pprint.pprint(my_kids)
# import itertools
# tpl = ("day1", "day2", "day3", "day4", "day5", "day6", "day7", "day8")
# dct = dict.fromkeys(tpl, "") # None by default
# pprint.pprint(dct)
# tpl2 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# z = zip(tpl, tpl2)
# print(dict(z))
# print(dict(itertools.zip_longest(tpl,tpl2, fillvalue=" ")))

# st = "12 23 4 53 6 7 4 99 8 7 56 3 42"
# my_dict = {int(key): int(key)*2 for key in st.split() if int(key)%2 == 0}
# print(my_dict)

# st = "Hello group qa2048, we are learning the Python, one of the greatest languages"
#
# def create_symbol_dict(input_st):
#     symbol_dict = {}
#     for sym in input_st:
#         if sym.lower() in symbol_dict:
#             symbol_dict[sym.lower()] += 1
#         else:
#             symbol_dict[sym.lower()] = 1
#     return symbol_dict
#
# # pprint.pprint(dict(sorted(create_symbol_dict(st).items(), key=lambda item: item[1])),sort_dicts=False)
# pprint.pprint({k: v for k, v in sorted(create_symbol_dict(st).items(), key=lambda item: item[1])}, sort_dicts=False)


# dct = {"brand": "Ford",
#        "model": "Mustang",
#        "year": 2005}
#
# # dct["model"] = "Bronco"
# dct.setdefault("model", "Bronco")
# dct.setdefault("color", "yellow")
# print(dct)

# num = [2, 18, 5, 7, 2, 32, 6, 9, 4, 8, 9, 4, 12, 14, 14, 5, 9] # count
#
# dct = {k: num.count(k) for k in num}
# print(dct)

# dct1 = {"item": "jacket", "size": "L", "color": "black"}
# dct2 = {"model": "35m1", "quantity": 50, "color": "blue"}
# new = {}
# for _ in dct1:
#     new.update(dct1.items())
# for _ in dct2:
#     new.update(dct2.items())
# print(new)

# print({**dct1, **dct2}) # union to one dictionary
# print(dct1, dct2) # two separate dictionaries

# interactive dictionary (vocabulary)
# words = {}
# with open("dictionary.txt", 'a+', encoding="utf8") as file:
#     file.seek(0)
#     lst = file.readlines()
#     for i in lst:
#         k, v = i[:-1].split(":")
#         words.update({k: v})
# # print(lst)
# # print(words)
# print("This is the interactive dictionary, that you create yourself\n"
#       "just enter a word... (for exit input 'q' button) ")
#
# while True:
#
#     w = input()
#     if w == 'q':
#         break
#     if w in words:
#         print(f"word {w} is translated as {words[w]}")
#     else:
#         with open("dictionary.txt", 'a+', encoding='utf8') as file:
#             words[w] = input("Input the translation in Russian: ")
#             file.write(f"\n{w}:{words[w]}")
#     print("enter a word... ")

# memory allocation and emptying with Garbage collector
# lst = [1, 2, 4]
# lst2 = lst
# del lst2
# del lst

# files handling

# f = open("test.txt")
# # print(type(f))
# # print(f)
# text = f.read()
# f.close()
# print(text)

# with open("test.txt") as file:
#     text = file.read()
#     print(type(file))
    # for each in file:
    #     print(each)
# print(text)
# print(type(text))

# for l in text:
#     print(l)
# with open("test.txt") as rf:
#     txt = rf.read(3)
#     txt2 = rf.read()
#     rf.seek(3)
#     txt3 = rf.read()
    # print(txt)
    # print(txt2)
    # print(txt3)

# l = ["This is Delhi\n", "This is Paris\n", "This is London\n"]
#
# with open("test.txt", 'a+') as af:
#     af.write("\nHello2\n") # EOF
    # af.seek(0)
    # print(af.readline(), end='')
    # print(af.readline(), end='')
    # af.writelines(l)
    # af.seek(0)
    # print(af.read())
    # lst = af.readlines() # list of lines
    # nlst = [el[:-1] for el in lst]
    # print(nlst)
    # print(af.tell())
    # af.seek(0)
    # print(*af.readlines()[4:8], sep='')


# with open("test.txt", 'w') as file:
#     file.write("Hello1")
#     file.read()

# with open("test1.txt", 'a+') as file:
#     file.write("Kuku")
#     file.seek(0)
#     file.read()

def count_words(st):
    words = {}
    for word in st.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words

def count_symbols(st):
    symbols = {}
    for char in st:
        if char in symbols:
            symbols[char] += 1
        else:
            symbols[char] = 1
    return symbols

with open("war.htm", encoding="utf8") as file:
    txt = file.read()


pprint.pprint(dict(sorted(count_words(txt.lower()).items(), key= lambda item: item[1])), sort_dicts=False)

# dct = count_words(txt.lower())
# lst = sorted(dct.items(), key= lambda item: item[1])
# sorted_dct = dict(lst)
# pprint.pprint(sorted_dct, sort_dicts=False)