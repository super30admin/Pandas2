import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    myset = set()
    for i in range(len(views)):
        if views['author_id'][i] == views['viewer_id'][i]:
            myset.add(views['author_id'][i])
             

    return pd.DataFrame(myset,columns = ['id']).sort_values(by = 'id')
    

#####################################################################
# def article_views(views: pd.DataFrame) -> pd.DataFrame:
#     df = views[views['author_id'] == views['viewer_id']]
#     #is_valid = views['author_id'] == views['viewer_id']
#     #print(is_valid)
#     df = df['author_id'].unique()
#     df = pd.DataFrame(df, columns = ['id'])
#     return df.sort_values(by = ['id'])

##################################################################
    