'''
iterate over rows in Pandas Dataframe using iterrows, itertuples
'''

# importing pandas
import pandas as pd

# list of dicts
input_df = [{'name':'Sujeet', 'age':10},
			{'name':'Sameer', 'age':11},
			{'name':'Sumit', 'age':12}]

df = pd.DataFrame(input_df)
print('Original DataFrame: \n', df)

# 1. Using iterrows function
print('\nRows iterated using iterrows() : ')
for index, row in df.iterrows():
	print(row['name'], row['age'])


# 2. Using itertuples function
print('\nRows iterated using itertuples() : ')
for row in df.itertuples():
    print(getattr(row, 'name'), getattr(row, 'age'))