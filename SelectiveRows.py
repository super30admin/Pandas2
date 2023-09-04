import pandas as pd

record = { 'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ], 'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'], 'Percentage': [88, 92, 95, 70, 65, 78] }

dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
result_df = dataframe[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', result_df)

# using loc
result_df = dataframe.loc[dataframe['Percentage'] > 80]

# inoptions
options = ['Math', 'Commerce']
result_df = dataframe[dataframe['Stream'].isin(options)]

# loc and inoptions
result_df = dataframe.loc[dataframe['Stream'].isin(options)]

# not in options
result_df = dataframe.loc[~dataframe['Stream'].isin(options)]

# selecting rows based on multiple conditions
result_df = dataframe[(dataframe['Age'] == 21) & dataframe['Stream'].isin(options)]

# selecting rows based on multiple conditions with loc
result_df = dataframe.loc[(dataframe['Age'] == 21) & dataframe['Stream'].isin(options)]