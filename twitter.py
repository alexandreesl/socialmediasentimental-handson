from config import *
from textblob import TextBlob
from nltk import downloader
import tweepy


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print('A TWEET!')
        print(status.text)
        print('AND THE SENTIMENT PER SENTENCE IS:')
        blob = TextBlob(status.text)
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)


auth = tweepy.OAuthHandler(consumerkey, consumerkeysecret)
auth.set_access_token(accesstoken, accesstokensecret)

downloader.download('punkt')

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=auth, listener=myStreamListener)

stream = tweepy.Stream(auth, myStreamListener)
stream.filter(track=['coca cola'], languages=['en'])
