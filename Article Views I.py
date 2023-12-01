import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    res_df = pd.DataFrame(df['author_id'].unique(), columns=['id'])
    return res_df.sort_values(by='id', ascending=True)
