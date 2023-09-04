import pandas as pd
df=pd.DataFrame({'Date':['10/1/2021','10/2/2021','10/3/2021','10/4/2021','10/5/2021'],
                 'product':[' UMbrella', ' maTtress', 'BaDmintoN ', 'Shuttle'],
                 'Updated_Price':[1250,1350,1450,1550],
                 'Discount':[10,15,20,25]})
print(df)

#creating custom function
def Format_data(df):
    for i in range(df.shape[0]):
        df.iat[i,1]=df.iat[i,1].strip().capitalize()
    Format_data(df)

#Using pandas Apply Function
df['product']=df['product'].apply(lambda x:x.strip().capitalize())
