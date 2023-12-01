import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['char_len'] = tweets['content'].apply(lambda x: len(x))
    res_df = tweets[tweets['char_len'] > 15]
    res = res_df['tweet_id']
    return pd.DataFrame(res, columns=['tweet_id'])
