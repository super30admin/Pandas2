
import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df.head())

#Stack:It is used to pivot the columns of a DataFrame into rows, effectively making it longer. It stacks the specified columns on top of each other.
import pandas as pd
df = pd.read_csv("nba.csv")

df_stacked = df.stack()
print(df_stacked.head(5))

#Unstack:It is used to pivot the index levels of a DataFrame into columns, effectively making it wider. It unstacks the specified index levels
import pandas as pd

df = pd.read_csv("nba.csv")
df_unstacked = df_stacked.unstack()
print(df_unstacked.head(10))

#Melt:

import pandas as p
df = pd.read_csv("nba.csv")

# it takes two columns "Name" and "Team" aS id_vars:These are the columns that you want to stay the same in the melted DataFrame. 
# They are the columns that you use to identify each observation or row.
df_melt = df.melt(id_vars =['Name', 'Team'])
print(df_melt.head(10))


