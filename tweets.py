import snscrape.modules.twitter as sntwitter
import pandas as pd
import time, sys

query = ' vestibular headache OR vestibular migraine OR vestibular OR migraine since:2000-01-01 until:2022-09-01 lang:"en" '
tweets = []
limit = sys.maxsize
counter = 0
start_time = time.time()

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    # print(vars(tweet))
    # break
    if len(tweets) == limit:
        break
    else:
        tweets.append([tweet.date, tweet.id, tweet.user.username, tweet.content, tweet.url])
        # can also ret outlinks, tcooutlinks, replycount, retweetcount, likecount..
        # https://github.com/igorbrigadir/twitter-advanced-search
    print(str(counter))
    counter +=1

print("Completed in %s seconds" % (time.time() - start_time))

df = pd.DataFrame(tweets, columns=['Datetime', 'Tweet ID', 'Username', 'Content', 'URL'])

df.to_csv('tweets_df2.csv')
