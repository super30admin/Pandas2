#Method 1: Using the index attribute of the Dataframe. 

import pandas as pd

data = {'Name': ['Ankit', 'Amit',
				'Aishwarya', 'Priyanka'],
		'Age': [21, 19, 20, 18],
		'Stream': ['Math', 'Commerce',
				'Arts', 'Biology'],
		'Percentage': [88, 92, 95, 70]}

df = pd.DataFrame(data, columns=['Name', 'Age',
								'Stream', 'Percentage'])

print("Given Dataframe :\n", df)

print("\nIterating over rows using index attribute :\n")

for ind in df.index:
	print(df['Name'][ind], df['Stream'][ind])

#  Method 2: Using loc[] function of the Dataframe. 
import pandas as pd


print("\nIterating over rows using loc function :\n")
for i in range(len(df)):
	print(df.loc[i, "Name"], df.loc[i, "Age"])
	

#  Method 3: Using iloc[] function of the DataFrame. 

print("\nIterating over rows using iloc function :\n")
for i in range(len(df)):
	print(df.iloc[i,0],df.iloc[i,2])
       
# Method 4: Using iterrows() method of the Dataframe. 

print("\nIterating over rows using iterrows() method :\n")
for index,row in df.iterrows():
	print(row['Name'],row['Age'])
	
#  Method 5: Using itertuples() method of the Dataframe. 
print("\nIterating over rows using itertuples() method :\n")
for row in df.itertuples(index=True,name='pandas'):
	print(getattr(row,'Name'),getattr(row,'percentage'))


#  Method 6: Using apply() method of the Dataframe. 
print("\nIterating over rows using apply function :\n")

print(df.apply(lambda row: row["Name"] + " " + 
               str(row["Percentage"]), axis=1))




