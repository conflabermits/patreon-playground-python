#!/usr/bin/env python3

'''
This script was initially lifted directly from the following documentation location:
https://docs.patreon.com/#fetch-a-creator-profile-and-campaign-info
It had to be modified to actually spit out printable json. Nice.
'''

import patreon
from local_creds import creator_access_token
import json

api_client = patreon.API(creator_access_token)
campaign_response = api_client.fetch_campaign()

#campaign = campaign_response.data()[0]
#print('campaign is', campaign)

#print('Campaign response data json:')
#print(json.dumps(campaign_response.json_data, indent=4))
campaign_response_json = json.dumps(campaign_response.json_data, indent=4)
print(f'Campaign response json:\n{campaign_response_json}')

#user = campaign.relationship('creator')
#print('user is', user)
#print('User data:')

print(f'\nPatreon Campaign Info:')

campaign_name = campaign_response.json_data['data'][0]['attributes']['name']
#print('\tCampaign Name: ' + campaign_name)
print(f'\tCampaign Name: {campaign_name}')

campaign_id = campaign_response.json_data['data'][0]['id']
print(f'\tCampaign ID: {campaign_id}')

campaign_headline = campaign_response.json_data['data'][0]['attributes']['creation_name']
print(f'\tCampaign Headline: {campaign_headline}')

campaign_url = campaign_response.json_data['data'][0]['attributes']['url']
print(f'\tCampaign URL: {campaign_url}')

creator_id = campaign_response.json_data['data'][0]['relationships']['creator']['data']['id']
#print('\tCreator ID: ' + creator_id)
print(f'\tCampaign Creator ID: {creator_id}')

print(f'\nFirst User:')

user_name = campaign_response.json_data['included'][0]['attributes']['full_name']
print(f'\tUsername: {user_name}')

vanity_name = campaign_response.json_data['included'][0]['attributes']['vanity']
print(f'\tAlternate Username: {vanity_name}')

user_id = campaign_response.json_data['included'][0]['id']
print(f'\tUser ID: {user_id}')
