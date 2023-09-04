import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 'Percentage': [88, 92, 95, 70]}

df = pd.DataFrame(data, columns=['Name', 'Age', 'Stream', 'Percentage'])

# using index
print("\nIterating over rows using index attribute :\n")
for ind in df.index:
	print(df['Name'][ind], df['Stream'][ind])

# using loc
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])

# using iloc
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 1])

# using iterrows
for index, row in df.iterrows():
    print(row["Name"], row["Age"])

# using itertuples
for row in df.itertuples(index=True, name='Pandas'):
    print(getattr(row, "Name"), getattr(row, "Percentage"))

# using apply function
print(df.apply(lambda row: row["Name"] + " " +  str(row["Percentage"]), axis=1))