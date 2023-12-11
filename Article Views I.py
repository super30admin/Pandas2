import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    df.drop_duplicates(subset=['author_id'],inplace=True)
    df.sort_values(by=['author_id'],inplace=True)
    return df[['author_id']].rename(columns={'author_id':'id'})


    # myset = set()
    # for i in range(len(views)):
    #     if views['author_id'][i] == views['viewer_id'][i]:
    #         if views['author_id'][i] not in myset:
    #             myset.add(views['author_id'][i])
    # return pd.DataFrame(myset, columns = ['id']).sort_values(by=['id'])