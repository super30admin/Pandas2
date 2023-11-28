import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:

    return tweets[tweets['content'].str.len() > 15][['tweet_id']]
    
    
    
    # lst = []
    # for i in range(len(tweets)):
    #     if len(tweets['content'][i]) > 15:
    #         lst.append(tweets['tweet_id'][i])
    # print(lst)
    # return pd.DataFrame(lst, columns = ['tweet_id'])


