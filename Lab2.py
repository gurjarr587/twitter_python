import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import twitter
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
from pandas.io.json import json_normalize
from itertools import cycle, islice
from textblob import TextBlob
import pip
pip.main(["install","twitter"])
pip.main(["install","textblob"])


ACCESS_TOKEN = "824049747493355520-QDDt06V9ciNgD2fR5SFSWHRsXWAaAHV"
ACCESS_SECRET = "To6smrFMUTq8KnqHQ6PMcjgflDDJvY6MfByqSiLUPaEQJ"
consumer_key = "OFnvORBQHqAUMd1uqZ6qK5UP5"
consumer_secret = "2FmAhqWWxG0GLhnnpIkkPcu28g65xhOZ9UFgKe9Gd4S9tF2lkE"
oauth = OAuth(ACCESS_TOKEN, ACCESS_SECRET, consumer_key, consumer_secret)
twitter = Twitter(auth=oauth)

q = 'earth'

search_results = twitter.search.tweets(q=q,count = 100)
df = json_normalize(search_results, 'statuses')

subjectivity = np.empty(1)
polarity = np.empty(1)


for x in df['text']:
    w = TextBlob(x)
    w.sentiment
    subjectivity =np.append(subjectivity,w.subjectivity)
    polarity=np.append(polarity,w.polarity)


df['polarity']=subjectivity[1:101]

hidf = df[(df['polarity']>=0.7) & (df['polarity']>=-0.7)]

hisn=json_normalize(hidf['entities'],'user_mentions')
print(hisn)
df2 = pd.DataFrame({'subjectivity':subjectivity,'polarity':polarity})
df2.plot()