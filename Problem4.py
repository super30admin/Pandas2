# Problem 4 : How to iterate over rows in Pandas Dataframe
# Method 1 -Using dataframe.iterrow() method

import pandas as pd

input_df=[{'name':'Sujeet','age':10},
          {'name': 'Akshatha','age':25},
          {'name':'Abhishek','age':23}]

df=pd.DataFrame(input_df)

print(df)

for index, row in df.iterrows():
    print(row['name'],row['age'])

#Method 2 -Dataframe.itertuples

df=pd.DataFrame(input_df)

for row in df.itertuples():
    print(getattr(row,'name'),getattr(row,'age'))