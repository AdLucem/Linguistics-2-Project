#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv, sys


#Twitter API credentials
consumer_key = "5zNNfrxU76kg1A0OLtXdE57MF"
consumer_secret = "2bXdEutp6S2IfhrTmw6PKlT4FmZzEK1YI7mYjHsciXHeja0zYj"
access_key = "858382850453676032-BTvrNFITgL7y8NBf6Op3QX4zkw3QWbh"
access_secret = "RTag4wIHA7mlYf1yXo78RN52bTrn5aKhkR4rZDWR7rAp2"


def get_all_tweets(screen_name, n):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
        #correction: only grabbing 1000 tweets per user
	while len(new_tweets) > 0 and len(alltweets) <= 1000 :
		print("getting tweets before %s" % (oldest))
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))

	
	#write into a text file	
	with open("twitter_%s.txt" % (n), 'w+') as f:
                for i in alltweets :
                        f.write(str(i.text.encode('utf-8')) + "  $^$  ")
                f.close()

if __name__ == '__main__':

        l_tweets = ["J_tsar","TheEllenShow","alanalevinson","audevwhite","Daniel_bearman","robesman","ladygaga","NiallOfficial","stevenbjohnson","Sockamillion"]
        get_all_tweets("TheEllenShow",15)
	#pass in the username of the account you want to download
#        for i in range(3,11) :
                
#	        get_all_tweets(l_tweets[i-1],i)
