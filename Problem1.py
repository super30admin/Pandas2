'''
1. We create a custom function to iterate over each row and modify the product value
2. We have apply function that applies a function over all rows. We use a lambda function to strip and capitalize each value in Product.
'''

# importing pandas as pd
import pandas as pd

# Create the dataframe
df = pd.DataFrame({'Date':['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
				'Product':[' UMbreLla', ' maTtress', 'BaDmintoN ', 'Shuttle'],
				'Updated_Price':[1250, 1450, 1550, 400],
				'Discount':[10, 8, 15, 10]})

# Print the dataframe
print(df)


# 1. Custom Function
def formatDf(df):
    for i in range(len(df)):
        df.iloc[i,1] = df.iloc[i,1].strip().capitalize()
    return df

formatted_df = formatDf(df)
print(formatted_df)

# 2. apply function
formatted_df = df
formatted_df['Product'] = df['Product'].apply(lambda x: x.strip().capitalize())
print(formatted_df)
