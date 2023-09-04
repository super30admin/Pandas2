import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    df = tweets[tweets['content'].str.len() > 15]
    return df[['tweet_id']].sort_values(by = ['tweet_id']).drop_duplicates()