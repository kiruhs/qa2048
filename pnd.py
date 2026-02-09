import pandas as pd

# lst = [1, 4.3, 'hello', True, [3, 5], (3, 'a')]
# lst2 = [1, 2, -234.8, 100]
# a = pd.array(lst)
# print(a)

# lst2 = [1, 2, -234.8, 100]
# myvar = pd.Series(lst2, index=['a', 'b', 'c', 'd'])
# # print(type(myvar))
# # print(pd.__version__)
#
# print(myvar)
# print(myvar['c'])

# calories = {'day1': 480, 'day2': 380, 'day3': 400, 'day4': 420}
# var = pd.Series(calories, dtype='int16')
# print(var)
# print(var.__sizeof__())

s1 = pd.Series(['100', '400', 'python', '200', '300.12'])
# print(s1)
s2 = pd.to_numeric(s1, errors='coerce')
# print(s2)
sorted_s = pd.Series(s2).sort_values(ascending=False)
print(sorted_s)