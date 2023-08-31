'''
Reshape a pandas DataFrame using stack,unstack and melt method
'''

import pandas as pd
df = pd.read_csv("nba.csv")
# Printing the first 5-rows
print(df.head())

# 1. Using stack method
df_stacked = df.stack()
print(df_stacked.head(26))

# 2. Unstack() method
df_unstacked = df_stacked.unstack()
print(df_unstacked.head())

# 3. melt method
df_melted = df.melt(id_vars=['Team','Age'],value_vars=['Name','Height'])
print(df_melted.tail(100))

