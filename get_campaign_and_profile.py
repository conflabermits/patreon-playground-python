#!/usr/bin/env python3

'''
This script was initially lifted directly from the following documentation location:
https://docs.patreon.com/#fetch-a-creator-profile-and-campaign-info
It had to be modified to actually spit out printable json. Nice.
'''

import patreon
from local_creds import *
import json

access_token = creator_access_token

api_client = patreon.API(access_token)
campaign_response = api_client.fetch_campaign()
#campaign = campaign_response.data()[0]
print(json.dumps(campaign_response.json_data, indent=4))
#print('campaign is', campaign)
#user = campaign.relationship('creator')
#print('user is', user)