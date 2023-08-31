'''
Selecting rows in pandas DataFrame based on conditions. loc, iloc, isin, filter
'''

# importing pandas
import pandas as pd

record = {

'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78] }

# create a dataframe
dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
print("Given Dataframe :\n", dataframe)

# 1. Based on condition filtering rows
rslt_df = dataframe[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)

# 2.Using loc method
rslt_df = dataframe.loc[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)

# Another condition
rslt_df = dataframe.loc[dataframe['Percentage'] != 80]
print('\nResult dataframe :\n', rslt_df)

# 3. Using isin method
options = ['Math', 'Commerce']
rslt_df = dataframe[dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

# loc and isin 
options = ['Math', 'Commerce']
rslt_df = dataframe.loc[dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

# 4. Getting records not satisfying condition
rslt_df = dataframe.loc[~dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

# 5. Combining filter conditions
rslt_df = dataframe.loc[~dataframe['Stream'].isin(options) & (dataframe['Age']!=21)]
print('\nResult dataframe :\n', rslt_df)

# Another example 
rslt_df = dataframe.loc[dataframe['Stream'].isin(options) & (dataframe['Age']==21)]
print('\nResult dataframe :\n', rslt_df)








