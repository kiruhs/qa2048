import pandas as pd
import numpy as np
from time import time
import requests
# lst = [1, 4.3, 'hello', True, [3, 5], (3, 'a')]
# lst2 = [1, 2, -234.8, 100]
# a = pd.array(lst)
# print(a)

# lst2 = [1, 2, -234.8, 100]
# myvar = pd.Series(lst2, index=['a', 'b', 'c', 'd'])
# # print(type(myvar))
# print(pd.__version__)
#
# print(myvar)
# print(myvar['c'])

# calories = {'day1': 480, 'day2': 380, 'day3': 400, 'day4': 420}
# var = pd.Series(calories, dtype='int16')
# print(var)
# print(var.__sizeof__())

# s1 = pd.Series(['100', '400', 'python', '200', '300.12'])
# print(s1)
# s2 = pd.to_numeric(s1, errors='coerce')
# print(s2)
# sorted_s = pd.Series(s2).sort_values(ascending=False)
# print(sorted_s)


# num = 9_999_990
# Max_num = 10_000_000
# l = [i for i in range(Max_num)]
# a = np.array(l)
# # print(l)
# # print(a)
#
# start = time()
# if num in l:
#     print(num)
# print(time() - start)
#
# start = time()
# if num in a:
#     print(num)
# print(time() - start)

# lst = [[1,2], [1,2],[4,5]]
# ar = np.array(lst)
# print(ar)

# write the program to get items of given series that not presented in another given series
# s1 = pd.Series([1,2,3,4,5])
# s2 = pd.Series([2,4,6,8,10])
# print("Original Series: ")
# print(s1.values)
# print("Items from s1 that aren't presented in s2: ")
# print(s1[~s1.isin(s2)].values)

# write a program to get the items which are not of two series

# s11 = pd.Series(np.union1d(s1, s2))
# # print(s11)
# s22 = pd.Series(np.intersect1d(s1, s2))
# # print(s22)
# result = s11[~s11.isin(s22).values]
# print(result)

# DataFrame - 2Dimension data structure

# lst = [[1, "John", 9.5], [2, "Mary", 9.1], [3, "Jeffry", 7.8]]
# df = pd.DataFrame(lst, columns=["#", "Name", "Score"])
# print(df)
# print(df["Score"].name)

# url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(PPP)_per_capita"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
# req = requests.get(url, headers=header)
# with open("page.html", 'w', encoding='utf8') as f:
#     f.write(req.text)
tbls = pd.read_html("page.html", encoding='utf8')
# print(type(tbls))
# print(tbls[1].info())
# print(tbls[1].describe())
# print(tbls[1].head(20))
# print(tbls[1].tail(20))
print(tbls[1].to_string(index=False)) # to hide indexes
