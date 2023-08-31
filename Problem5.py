'''
Different ways to iterate over rows in Pandas Dataframe: loc, iloc, forloop on index, iterrows, itertuples, apply
'''

# import pandas package as pd
import pandas as pd

# Define a dictionary containing students data
data = {'Name': ['Ankit', 'Amit',
				'Aishwarya', 'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce',
				'Arts', 'Biology'],
		'Percentage': [88, 92, 95, 70]}
# Convert the dictionary into DataFrame
df = pd.DataFrame(data, columns=['Name', 'Age',
								'Stream', 'Percentage'])
print("Given Dataframe :\n", df)

print("\nIterating over rows using index attribute :\n")
# 1. Each row with a for loop
for ind in df.index:
	print(df['Name'][ind], df['Stream'][ind])

# 2. Using loc function
print("\nIterating over rows using loc function :\n")  
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])

# 3. Using iloc function
print("\nIterating over rows using iloc function :\n")  
for i in range(len(df)):
    # print(df.iloc[i]["Name"], df.loc[i]["Age"])
    print(df.iloc[i, 0], df.iloc[i, 2])

# 4. Using iterrows function
print("\nIterating over rows using iterrows() method :\n")
for index, row in df.iterrows():
	print(row['Name'], row['Age'])
      
# 5. Using itertuples function
print("\nIterating over rows using itertuples() method :\n")
for row in df.itertuples():
	print(getattr(row,'Name'),getattr(row,'Age'))
	
# 6. Using apply function
print("\nIterating over rows using apply() method :\n")
print(df.apply(lambda row: row["Name"] + " " + 
               str(row["Percentage"]), axis=1))

      

