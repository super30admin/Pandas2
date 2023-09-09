#Problem 1 : Clean the string data in the given Pandas Dataframe 
import pandas as pd
df = pd.DataFrame({'Players':['JoHn','bEN','JuStIN'],'Games':[5,4,6]})
df['Players'] = df['Players'].apply(lambda x : x.strip().capitalize())
print(df)

#Problem 2 : Reindexing in Pandas DataFrame
index = [1,2,3]
df = pd.DataFrame({'Player':['Dhoni','Virat','Ganguli'],'Centuries':[200,170,201]},index=index)
new = [3,2,1,4]
print(df.reindex(new,fill_value='N/A'))

#Problem 3 : Reshape a pandas DataFrame using stack,unstack and melt method
index =[1,2,3]
df = pd.DataFrame({'Player':['Dhoni','Virat','Ganguli'],'Centuries':[200,170,201],'Age':[40,35,45]},index=index)
df_stacked = df.stack()
print(df_stacked)
df_unstacked = df_stacked.unstack()
print(df_unstacked)
df_melt = df.melt(id_vars =['Player','Age'])
print(df_melt)

#Problem 4 : How to iterate over rows in Pandas Dataframe
input_df = [{'name':'Taylor', 'age':35},
            {'name':'Selena', 'age':25}, {'name':'Hayley', 'age':40}]
df = pd.DataFrame(input_df)
print(df)

print('With itertuples')
for row in df.itertuples():
    print(getattr(row, 'name'), getattr(row, 'age'))

#Problem 5 : Different ways to iterate over rows in Pandas Dataframe
input_df = [{'Name':'Taylor', 'Age':35},
            {'Name':'Selena', 'Age':25},
            {'Name':'Hayley', 'Age':40}]
df = pd.DataFrame(input_df)
print("Method 1:")
for ind in df.index:
    print(df['Name'][ind], df['Age'][ind])

print("\nMethod 2:")
for i in range(len(df)):
    print(df.loc[i, "Name"], df.loc[i, "Age"])
    
print("\nMethod 3:")
for i in range(len(df)):
    print(df.iloc[i, 0], df.iloc[i, 1])
 
print("\nMethod 4:")
for index, row in df.iterrows():
    print(row["Name"], row["Age"])
   
print("\nMethod 5:")
print(df.apply(lambda row: row["Name"] + " " + 
               str(row["Age"]), axis=1))
#Problem 6 : Selecting rows in pandas DataFrame based on conditions
input_df = [{'Name':'Taylor', 'Age':35, 'Percentage':90},
            {'Name':'Selena', 'Age':25, 'Percentage':95},
            {'Name':'Hayley', 'Age':40, 'Percentage':70}]
df = pd.DataFrame(input_df)
result = df.loc[df['Percentage'] > 80]
print('\nResult :\n', result)
