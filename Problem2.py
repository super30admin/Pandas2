# Problem 2 : Reindexing in Pandas DataFrame
import pandas as pd
import numpy as np

column=['a','b','c','d','e']
index=['A','B','C','D','E']

df=pd.DataFrame(np.random.rand(5,5), columns=column,index=index)

print(df)

df1=df.reindex(['B','A','C','E','D'])
print(df1)