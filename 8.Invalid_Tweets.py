import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
  isValid=tweets['content'].str.len()>15
  df=tweets[isValid]
  return df[['tweet_id']]