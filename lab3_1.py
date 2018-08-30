import pip
pip.main(["install","twitter"])
import json
from twitter import Twitter
from twitter import OAuth
from twitter import TwitterHTTPError
from twitter import TwitterStream
import pandas as pd
from pandas.io.json import json_normalize



AccessToken = '2453223655-cAGydCEyUcRKofnQo52zoZzzqOMQdIZth3AdKI2'//bhai json key kyo daal rhkii he hta isko kiski twitter id h ye......
AccessSecret = 'gqUjZmM67a3Dz86VXjzIFRSq3M5XvxKEsTcc1NCrRcsWU'//bhai json key kyo daal rhkii he hta isko kiski twitter id h ye......
ConsumerKey = '3CDW01XTifhX0k0OyOZ5UisTb'//bhai json key kyo daal rhkii he hta isko kiski twitter id h ye......
ConsumerSecret = 'YVBfDyjwuXO9xNrG2vKhgLy4wE9ntMvkLMfFEBsjP41ecuXOQo'//hta

oauth=OAuth(AccessToken, AccessSecret, ConsumerKey, ConsumerSecret)
twitter_api=Twitter(auth=oauth)

nashville_trends= twitter_api.trends.place(_id=2457170)
NYC_trends= twitter_api.trends.place(_id=2459115)


df1=json_normalize(NYC_trends,'trends')
df1[['name','tweet_volume']].plot(kind='bar')
NYCdf = df1.sort_index(by=[ 'tweet_volume'], ascending=False)
print(NYCdf.head(30))



df2=json_normalize(nashville_trends,'trends')
df2[['name','tweet_volume']].plot(kind='bar')
nashvilledf = df2.sort_index(by=[ 'tweet_volume'], ascending=False)
print(nashvilledf.head(30))
