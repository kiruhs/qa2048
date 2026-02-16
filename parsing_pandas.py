from time import sleep

from sqlalchemy.dialects.mssql.information_schema import columns
from tabulate import tabulate
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# df = pd.read_csv("globes.csv", encoding='utf8')
# print(df.head(1))
# print(df.iloc[10:31])
# print(df.iloc[185:, 2:].to_string(index=False))
# print(df.to_string(index=False))
# new_df = df.dropna()
# print(new_df)
# df.dropna(inplace=True)
# print(df)
# print(type(df.iloc[1, -1]))
# print(df.iloc[:,-1].to_string(index=False))
# df['נפח מסחר ב- ₪'] = df['נפח מסחר ב- ₪'].str.replace(',', '').astype(float)
# df['שער עסקה'] = df['שער עסקה'].str.replace(',', '').astype(float)
# df['col7'] = df.loc[2:]['col7'].str.replace(',', '')
# print(type(df.iloc[1,-1]))

# df1 = df.iloc[:][df.iloc[:, -1] > 5_000 ]
# print(df1.reset_index(drop=False))

# print(tabulate(df1, headers='keys', tablefmt='psql'))

# print(df1['שער עסקה'].mean())
# print(df1['נפח מסחר ב- ₪'].sum())
# print(df1['נפח מסחר ב- ₪'].max())
#
# # df1['נפח מסחר ב- ₪'].plot()
# df1['שער עסקה'].plot()
# plt.savefig("stock.png")
# plt.show()

# df = pd.DataFrame(np.arange(12).reshape(3, 4), columns=['a', 'b', 'c', 'd'])
# print(df)

# df.drop(columns = ['b', 'c'], inplace=True)

# print(df.drop(['b', 'c'], axis=1))
# print(df.drop([0, 2], axis=0))
# print(df)

# df = pd.DataFrame({ 'X': [100, 100, 100, 90, 80, 90, 10],
#                     'Y': ['Alex', 'Jane', 'Svetlana', 'Andrey', 'Elena', 'Gleb', 'Gregory'],
#                     'Z': [22234, 24230, 13426, 22547, 12345, 12340, 43210]
#                     })
# print(df)
#
# print(df.groupby('X').aggregate(lambda tdf: tdf.unique().tolist()))

# df = pd.DataFrame( {
#     'id': [1, 1, 2, 3, 3, 4, 4, 4],
#     'value': ['a', 'a', 'b', None, 'a', 'a', None, 'b']
# })
# print(df)
#
# print(df.groupby('value')['id'].nunique())

# df = pd.DataFrame({
#     'ord_no': [70001, 70009, 70002, 70004, 70007, 70005, 70008, 70010, 70003, 70012, 70011, 70013],
#     'purchase_amt': [150.5, 270.65, 65.26, 100.5, 948.5, 2400.6, 5760, 1983.43, 2480.4, 250.45, 75.29, 3045.6],
#     'ord_date': ['05-10-2012', '09-10-2012', '05-10-2012', '08-17-2012', '10-09-2012', '07-27-2012', '10-09-2012', '10-10-2012', '10-10-2012', '06-17-2012', '07-08-2012', '04-25-2012'],
#     'customer_id': ['C3001', 'C3001', 'D3005', 'D3001', 'C3005', 'D3001', 'C3005', 'D3001', 'D3005', 'C3001', 'D3005', 'D3305'],
#     'salesman_id': [5002, 5005, 5001, 5003, 5002, 5001, 5001, 5006, 5003, 5002, 5007, 5001]
# })
# print(df)
# print("==================================================")
# # split the dataset into groups on salesman and calculate the number of customers starting with 'C', the list of all products
# # and the difference between maximum purchase and minimum purchase amount
#
# def customer_id_C(x):
#     return (x.str[0] == 'C').sum()
#
# result = df.groupby(['salesman_id']).agg(customer_id_C = ('customer_id', customer_id_C),
#                                         customer_id_list= ('customer_id', lambda x: ','.join(x)),
#                                         purchase_amt_gap= ('purchase_amt', lambda x: x.max()-x.min()),
#                                         customer_id_C_list = ('customer_id', lambda x: ','.join(name for name in x if name.startswith('C')))
#                                         )
#
# print(result.to_string())


df = pd.read_csv("data.csv")
for index, row in df.iterrows():
    print(index, " and ", row)