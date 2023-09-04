import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df =  df[['author_id']].sort_values(by = ['author_id']).rename(columns = {'author_id':'id'})
    df = df.drop_duplicates()
    return df