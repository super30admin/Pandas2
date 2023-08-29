#  Problem 1 : Clean the string data in the given Pandas Dataframe
import pandas as pd
df=pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', '  maTtress', 'BaDmintoN ', 'Shuttle'],
                   'Updated_Price':[1250, 1450, 1550, 400],
                   'Discount':[10, 8, 15, 10]})

df['Product']=df['Product'].apply(lambda x: x.strip().capitalize())

print(df)