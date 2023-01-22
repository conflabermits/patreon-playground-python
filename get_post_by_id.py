#!/usr/bin/env python3

'''
Pulling a Patreon campaign post

Post attributes and relationships: https://docs.patreon.com/#post-v2

GET /api/oauth2/v2/posts/{id}
Get a particular Post by ID. Requires the campaigns.posts scope.
(https://docs.patreon.com/#get-api-oauth2-v2-posts-id)
'''

'''
import patreon
from local_creds import creator_access_token
import json
import argparse
import sys
sys.dont_write_bytecode = True

parser = argparse.ArgumentParser(
    description = 'Get Patreon post data'
)
parser.add_argument(
    "-i",
    "--id",
    type = str,
    help = "Post ID of specific Patreon post",
    required = False
)
args = parser.parse_args()

access_token = creator_access_token
api_client = patreon.API(access_token)
#campaign_response = api_client.fetch_campaign()
'''

'''
Rough outline:
* Request post by ID
* For each top-level comment on post:
  * Grab post text, post hearts/likes, and poster's username (maybe post created time too)
  * Toss those in a list
* Sort the list by number of hearts/likes
* Print the top 10 posts
'''

# See Scripts/python/reddit/getKarmaConflabermits.py for a personal example of an oauth request

''' Borrowed from my reddit getKarmaConflabermits.py script
client_auth = requests.auth.HTTPBasicAuth(reddit_client_id, reddit_client_secret)
post_data = {"grant_type": "password", "username": reddit_username, "password": reddit_password}
headers = {"User-Agent": "3dsDeals-Checkbot/0.1 by conflabermits"}
response = requests.post("www.patreon.com/oauth2/authorize", auth=client_auth, data=post_data, headers=headers)
jresponse = response.json()
headers['Authorization'] = 'bearer ' + jresponse["access_token"]
#{'Authorization': 'bearer XXXXXXXXXXXXXXXXXXXXXXXX', 'User-Agent': '3dsDeals-Checkbot/0.1 by conflabermits'}
myinfo_response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
myinfo_jresponse = myinfo_response.json()
#print("Comment Karma: {myinfo_jresponse['comment_karma']} ; Link Karma: {myinfo_jresponse['link_karma']}")
print("Comment Karma: {x} ; Link Karma: {y}".format(x=myinfo_jresponse['comment_karma'],y=myinfo_jresponse['link_karma']))
'''

''' From python-patreon docs
GET www.patreon.com/oauth2/authorize
    ?response_type=code
    &client_id=<your client id>
    &redirect_uri=<one of your redirect_uris that you provided in step 1>
    &scope=<optional list of requested scopes>
    &state=<optional string>
'''

import requests
import requests.auth
from local_creds import creator_access_token

campaign_id = 9843936
headers = {'Authorization': 'bearer ' + creator_access_token}
response = requests.get(f'https://www.patreon.com/api/oauth2/v2/campaigns/{campaign_id}/posts') #gets a 401 right now
print(f'Hold...')
