'''
1. We reindexed the rows in first example by passing new indices to reindex. Default axis is row.
2. We reindexed the columns by passing axis = colummn in this case. 
3. If any unknown columns/rows are passed, NaNs arise and can be given default value using fill_value parameter in reindex function.
'''
# import numpy and pandas module
import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']

df1 = pd.DataFrame(np.random.rand(5,5),columns=column, index=index)
print(df1)

# 1. Reindexing the rows
print('\n\nDataframe after reindexing rows: \n',
df1.reindex(['B', 'D', 'A', 'C', 'E']))

# Passing index as a list
new_index =['U', 'A', 'B', 'C', 'Z']
print(df1.reindex(new_index))


# 2. Reindexing the columns
column=['e','a','b','c','d']
print(df1.reindex(column, axis='columns'))

# 3. Unknown column indices -> gives NaNs in those columns
column=['a','b','c','g','h']
print(df1.reindex(column, axis='columns'))

# 4. Replace NaNs using fill_value function
column=['a','b','c','g','h']
print(df1.reindex(column, axis='columns',fill_value=0))

# Replacing the missing data with a string
column=['a','b','c','g','h']
print(df1.reindex(column, axis='columns',fill_value='I am missing'))




