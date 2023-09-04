import pandas as pd
# using stack method
df = pd.read_csv("nba.csv")
df_stacked = df.stack()

# using unstack
df_unstacked = df_stacked.unstack()

# using melt
df_melt = df.melt(id_vars =['Name', 'Team'])
