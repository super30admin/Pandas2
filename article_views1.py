import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id']==views['viewer_id']]
    return df[['author_id']].rename({'author_id':'id'}, axis=1).sort_values(by=['id']).drop_duplicates()
    