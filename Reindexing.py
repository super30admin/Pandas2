import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']

df1 = pd.DataFrame(np.random.rand(5,5), columns=column, index=index)

print('\nDataframe after reindexing rows: \n', df1.reindex(['B', 'D', 'A', 'C', 'E']))
df1.reindex(['B', 'D', 'A', 'E', 'C'])

column = ['e', 'a', 'b', 'c', 'd']
print(df1.reindex(column, axis='columns'))

column = ['a', 'b', 'c', 'g', 'h']
# create the new index for columns
print(df1.reindex(column, axis='columns', fill_value=1.5))