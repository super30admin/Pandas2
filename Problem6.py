# Problem 6 : Selecting rows in pandas DataFrame based on conditions

import pandas as pd

record = {

'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78] }


dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])

print(dataframe)

result_df=dataframe[dataframe['Percentage']>80]
print(result_df)

resultdf=dataframe.loc[dataframe['Percentage']>80]
print(resultdf)

rslt=dataframe[dataframe['Percentage']!=95]
print(rslt)

options = ['Math', 'Commerce']

rslt_df=dataframe.loc[dataframe['Stream'].isin(options)]
print(rslt_df)

finaldf=dataframe[(dataframe['Age']==21)&(dataframe['Stream'].isin(options))]
print(finaldf)