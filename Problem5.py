# Problem 5 : Different ways to iterate over rows in Pandas Dataframe

import pandas as pd
data = {'Name': ['Ankit', 'Amit','Aishwarya', 'Priyanka'],
        'Age': [21, 19, 20, 18],
        'Stream': ['Math', 'Commerce','Arts', 'Biology'],
        'Percentage': [88, 92, 95, 70]}
  
df = pd.DataFrame(data, columns=['Name', 'Age', 
                                 'Stream', 'Percentage'])
  
print(df)

for ind in df.index:
    print(df['Name'] [ind],df['Stream'][ind])

# Method 2 using loc[]
for i in range(len(df)):
    print(df.loc[i,'Name'],df.loc[i,'Age'])


# Method 3 using iloc[]

for i in range(len(df)):
    print(df.iloc[i,0],df.iloc[i,2])
