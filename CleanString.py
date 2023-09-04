import pandas as pd

# Using lambda function
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
				    'Updated_Price':[1250, 1450, 1550, 400],
				    'Discount':[10, 8, 15, 10]})

df['Product'] = df['Product'].apply(lambda x: x.strip().capitalize())


# Using Customized function

df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
				    'Updated_Price':[1250, 1450, 1550, 400],
				    'Discount':[10, 8, 15, 10]})

def Format_data(df):
	for i in range(df.shape[0]):
        df.iat[i, 1]= df.iat[i, 1].strip().capitalize()

Format_data(df)
print(df)
