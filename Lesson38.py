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

from sqlalchemy.util import symbol

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
# # pprint.pprint(sorted(create_symbol_dict(st).items(), key=lambda item: item[1]))
# pprint.pprint({k: v for k, v in sorted(create_symbol_dict(st).items(), key=lambda item: item[1])})


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

dct1 = {"item": "jacket", "size": "L", "color": "black"}
dct2 = {"model": "35m1", "quantity": 50, "color": "blue"}
# new = {}
# for _ in dct1:
#     new.update(dct1.items())
# for _ in dct2:
#     new.update(dct2.items())
# print(new)

print({**dct1, **dct2}) # union to one dictionary
print(dct1, dct2) # two separate dictionaries