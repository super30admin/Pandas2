# Problem 3 : Reshape a pandas DataFrame using stack,unstack and melt methods
# import pandas module
import pandas as pd

# making dataframe
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

# it was print the first 5-rows
print(df.head())

#1. reshape the dataframe using stack() method
df_stacked = df.stack()
 
print(df_stacked.head(26))

# 2.# unstack() method
df_unstacked = df_stacked.unstack()
print(df_unstacked.head(10))

#3. Using melt() method 
# it takes two columns "Name" and "Team"
df_melt = df.melt(id_vars =['Name', 'Team'])
print(df_melt.head(10))
