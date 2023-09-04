#Reindexing the Rows

import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']
df1=pd.DataFrame(np.random.rand(5,5),columns=column,index=index)
print(df1)
print('\n\nDataframe after reindexing rows: \n',df1.reindex(['B','D','A','C','E']))

#2nd example
new_index =['U', 'A', 'B', 'C', 'Z']
print(df1.reindex(new_index))

#Reindexing the columns using the axis keyword
import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']
df1=pd.DataFrame(np.random.rand(5,5),columns=column,index=index)
column=['e','a','b','c','d']
print(df1.reindex(column, axis='columns'))

column =['a', 'b', 'c', 'g', 'h']
print(df1.reindex(column, axis ='columns'))

#Replacing the missing values
column =['a', 'b', 'c', 'g', 'h']
print(df1.reindex(column, axis ='columns', fill_value = 1.5))

#Replacing the missing values with string
print(df1.reindex(column, axis ='columns', fill_value = 'data missing'))
