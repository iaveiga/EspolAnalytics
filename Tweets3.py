# -*- coding: latin-1 -*-
import simplejson
from urllib import request
import re
import string
import unicodedata

def getTweets(user,nTweets):
    tweets = []
    url = "http://api.twitter.com/1/statuses/user_timeline.json?screen_name=%s&count=%s&include_rts=true" % (user, nTweets)
    file = request.urlopen(url)
    content = file.read()
    json = simplejson.loads(content)
    for js_tweet in json:
        tweets.append(js_tweet['text'].lower())
    return cleanTweets(tweets)
    #Retorna una lista de tweets en texto

def cleanTweets(ls):
    '''
        Recibe una lista de tweets, elimina los RT, mentions, links, dígitos
        símbolos de puntuación
    '''
    pRT = "(RT|via)((?:\\b\\W*@\\w+)+)"
    pMentions = "@\\w+"
    pPunct = "[[:punct:]]"
    pDig = "\d+"
    pLinks = '(?:http://|www.)[^"\' ]+'
    for i in range(0,len(ls)):
       ls[i] = cleanTweet(ls[i], pRT)
       ls[i] = cleanTweet(ls[i], pMentions)
       ls[i] = cleanTweet(ls[i], pPunct)
       ls[i] = cleanTweet(ls[i], pDig)
       ls[i] = cleanTweet(ls[i], pLinks)
    return ls

def cleanTweet(tweet,pattern):
    tweet = re.sub(pattern,'',tweet)
    return tweet
