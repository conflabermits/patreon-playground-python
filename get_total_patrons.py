#!/usr/bin/env python3

'''
This script was more-or-less lifted directly from the following post:
https://www.patreondevelopers.com/t/python-api2-how-to-get-all-active-patrons/4820
I needed a script to verify my Patreon credentials worked and this did the trick.
Only line I added was the 'from local_creds' so I wouldn't need to hard-code a token anywhere.
'''

import patreon
from local_creds import *

access_token = creator_access_token
api_client = patreon.API(access_token)

campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

all_pledges = []
cursor = None

while True:
   pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
   cursor = api_client.extract_cursor(pledges_response)
   all_pledges += pledges_response.data()
   if not cursor:
       break

print(len(all_pledges))

