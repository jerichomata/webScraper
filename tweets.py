import snscrape.modules.twitter as sntwitter
import pandas as pd

query = ' vestibular migraines headaches since:2012-01-01 until:2022-04-10 lang:"en" '
tweets = []
limit = 8000

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.user.username, tweet.content, tweet.url])

df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet ID', 'Username', 'Content', 'URL'])
df.to_csv('tweets_df.csv')
