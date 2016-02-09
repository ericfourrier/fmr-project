#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Author : eric fourrier

Purpose : Simple demo with of the kind of infos you can get with twitter api
"""

# Import Packages
import os
import tweepy
from utils import json


def get_consumer_tokens():
    """ Return a tuple of consumer_id, consumer_secret """
    return os.environ.get('TWITTER_CONSUMER_ID'), os.environ.get('TWITTER_CONSUMER_SECRET')


def get_access_tokens():
    """ Return a tuple of access_id, access_secret """
    return os.environ.get('TWITTER_ACCESS_ID'), os.environ.get('TWITTER_ACCESS_SECRET')


def authentify(consumer_id, consumer_secret, access_id, access_secret):
    auth = tweepy.OAuthHandler(consumer_id, consumer_secret)
    #auth.secure = True
    auth.set_access_token(access_id, access_secret)
    return auth


def authentify_app(consumer_id, consumer_secret):
    """ Identify only app increase rate limit to 450 for search"""
    return tweepy.AppAuthHandler(consumer_id, consumer_secret)


# ci, cs = get_consumer_tokens()
# auth = authentify_app(ci, cs)
# api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
# user = api.get_user('cagnol')
if __name__ == "__main__":
    # Assume your tokens are stored as environnement variables
    ci, cs = get_consumer_tokens()
    auth = authentify_app(ci, cs)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    john_cagnol = api.get_user('cagnol')
    write_to_json(john_cagnol._json, "john_cagnol.json")
