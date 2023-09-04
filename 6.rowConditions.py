#code-1: Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using basic method.

import pandas as pd

record = {
'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78] }

dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
print("Given Dataframe :\n", dataframe)
rslt_df = dataframe[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)

#code-2: Selecting all the rows from the given dataframe in which ‘Percentage’ is greater than 80 using loc[].

rslt_df = dataframe.loc[dataframe['Percentage'] > 80]
print('\nResult dataframe :\n', rslt_df)

#code-3 : Selecting all the rows from the given dataframe in which ‘Percentage’ is not equal to 95 using loc[].

rslt_df = dataframe.loc[dataframe['Percentage'] != 95]
print('\nResult dataframe :\n', rslt_df)

#code-4:Selecting those rows whose column value is present in the list using isin() method of the dataframe.

import pandas as pd
record = {
'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka', 'Priya', 'Shaurya' ],
'Age': [21, 19, 20, 18, 17, 21],
'Stream': ['Math', 'Commerce', 'Science', 'Math', 'Math', 'Science'],
'Percentage': [88, 92, 95, 70, 65, 78]}


dataframe = pd.DataFrame(record, columns = ['Name', 'Age', 'Stream', 'Percentage'])
print("Given Dataframe :\n", dataframe)
options = ['Math', 'Commerce']
rslt_df = dataframe[dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

#Code-5 :Selecting all the rows from the given dataframe in which ‘Stream’ is present in the options list using loc[].

rslt_df = dataframe.loc[dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

#code-6 : Selecting all the rows from the given dataframe in which ‘Stream’ is not present in the options list using .loc[].

options = ['Math', 'Science']
rslt_df = dataframe.loc[~dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

#code-7 :Selecting rows based on multiple column conditions using '&' operator.
options = ['Math', 'Science']
rslt_df = dataframe[(dataframe['Age'] == 21) &
          dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)

#Code-8: Selecting all the rows from the given dataframe in which ‘Age’ is equal to 21 and ‘Stream’ is present in the options list using .loc[].
ptions = ['Math', 'Science']
rslt_df = dataframe.loc[(dataframe['Age'] == 21) &
          dataframe['Stream'].isin(options)]
print('\nResult dataframe :\n', rslt_df)



