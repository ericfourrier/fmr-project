#!/usr/bin/env python
# -*- coding: utf-8 -*-u

"""
Author : eric fourrier

Purpose : Simple demo with of the kind of infos you can get with github api

Notes :
* If you want to use the script you have to put configure your gihub token as a
environnement variable.
"""

import os
import math
import time
from github import Github

from utils import write_to_json

def get_my_key(name = "GITHUB_API_KEY"):
    """ Get your github key stored on your bash_profile """
    return os.environ.get(name)

class GithubApiQuery(object):
    basic_rate_linit = 5000
    search_rate_linit = 30

    def __init__(self,token):
        self.token = token
        self._manager = Github(login_or_token=self.token)


    @property
    def rate_limit(self):
        return self._manager.rate_limiting[0]

    @property
    def resetime(self):
        """ Return the nb seconds to wait for next reset of 5000 calls (truncated to seconds)"""
        return self._manager.rate_limiting_resettime - int(time.time())


    def get_user(self, name):
        """
        Return github.NamedUser.NamedUser class for user with name like 'acreux'
         """
        return self._manager.get_user(name)

if __name__ == "__main__":
    key = get_my_key()
    g = GithubApiQuery(key)
    guido = g.get_user("gvanrossum")
    write_to_json(guido.raw_data, "Guido.json")
