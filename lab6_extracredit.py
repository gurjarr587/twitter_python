import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import pip
pip.main(["install","yelp"])

ConsumerKey ="SRiuGEp-1s18Pwh21KT4HA"
ConsumerSecret = "hBo_z8uvM7TCtUNaMKtOvyo_An8"
Token ="_xYsQ3WCoZhC9gWHqR876FxQmI_IyvL0"
TokenSecret ="HlGx83l3Yojp0h3NpMr8w7-mHPk"

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from pandas.io.json import json_normalize
import numpy as np
import pandas as pd
from textblob import TextBlob

auth = Oauth1Authenticator(
    consumer_key=ConsumerKey,
    consumer_secret=ConsumerSecret,
    token=Token,
    token_secret=TokenSecret
)

api = Client(auth)

df1 = pd.DataFrame()
df2 = pd.DataFrame()
def func1(off_set):
    params = {"term":"Indian","lang":"en","limit":200,"offset":off_set,"sort":1}
    val = api.search("New York",params)
    val.businesses
    df1 = pd.DataFrame()
    for v in val.businesses:
        df = pd.Series([v.name, v.snippet_text])
        df1= df1.append(df, ignore_index=True)
    return df1

df2 = df2.append(func1(0), ignore_index=True)
df2 = df2.append(func1(20), ignore_index=True)
df2 = df2.append(func1(40), ignore_index=True)
df2.shape
df2.head()

df2.columns = ['Name', 'Reviews']
sub = np.empty(0)
polar = np.empty(0)

for x in df2['Reviews']:
     w = TextBlob(x)
     w.sentiment
     sub=np.append(sub,w.subjectivity)
     polar=np.append(polar, w.polarity)

df2['Polarity'] = polar
df2['Subjectivity'] = sub
df2.head()
import matplotlib.pyplot as plt
df2.plot(x='Name', rot =90, kind='bar', figsize=(20,10))