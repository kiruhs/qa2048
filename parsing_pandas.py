from tabulate import tabulate
import pandas as pd
import numpy as np

df = pd.read_csv("globes.csv", encoding='utf8')
# print(df.head(1))
# print(df.iloc[10:31])
# print(df.iloc[185:, 2:].to_string(index=False))
# print(df.to_string(index=False))
# new_df = df.dropna()
# print(new_df)
df.dropna(inplace=True)
# print(df)
# print(type(df.iloc[1, -1]))
# print(df.iloc[:,-1].to_string(index=False))
df['נפח מסחר ב- ₪'] = df['נפח מסחר ב- ₪'].str.replace(',', '').astype(float)
df['שער עסקה'] = df['שער עסקה'].str.replace(',', '').astype(float)
# df['col7'] = df.loc[2:]['col7'].str.replace(',', '')
# print(type(df.iloc[1,-1]))

df1 = df.iloc[:][df.iloc[:, -1] > 5_000 ]
# print(df1.reset_index(drop=False))

# print(tabulate(df1, headers='keys', tablefmt='psql'))

print(df1['שער עסקה'].mean())
print(df1['נפח מסחר ב- ₪'].sum())
print(df1['נפח מסחר ב- ₪'].max())
