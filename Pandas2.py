#Question 1 :

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[(views['author_id'] == views['viewer_id'])]
    views.drop_duplicates('author_id' , inplace = True )
    views.sort_values(by = 'author_id', inplace = True )
    views = pd.DataFrame(views)
    return views[['author_id']].rename(columns = {'author_id': 'id'})

#Question 2 :


    return pd.DataFrame(tweets['tweet_id'])