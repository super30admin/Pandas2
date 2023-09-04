import pandas as pd

input_df = [{'name':'Sujeet', 'age':10}, {'name':'Sameer', 'age':11}, {'name':'Sumit', 'age':12}]
df = pd.DataFrame(input_df)

# iterate with iterrows()
for index, row in df.iterrows():
	print(row['name'], row['age'])

# iterate with itertuples()
for row in df.itertuples():
    print(getattr(row, 'name'), getattr(row, 'age'))