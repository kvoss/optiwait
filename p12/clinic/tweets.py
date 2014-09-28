import twitter
import json

# XXX: Go to http://dev.twitter.com/apps/new to create an app and get values   
# for these credentials, which you'll need to provide in place of these           
# empty string values that are defined as placeholders.                           
# See https://dev.twitter.com/docs/auth/oauth for more information                
# on Twitter's OAuth implementation.                                              

CONSUMER_KEY = 'lMk5wnSsEqRFqB6wTyQ00TlLk'
CONSUMER_SECRET ='A0XRy7zkgFej4fnTNqbKLF4QOhIRU6ygIul00JVYGE84BpPsO5'
OAUTH_TOKEN = '2835226370-1kIFZSqIsw9obeEFPGlkFhj3vwpSLna4aVcrCYK'
OAUTH_TOKEN_SECRET = 'NfAQTO3S2bQV4t95L6u3L71oZmtbhzjcfT9BXbgsjQ1fZ'

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                           CONSUMER_KEY, CONSUMER_SECRET)

twitter_api = twitter.Twitter(auth=auth)

def get_msgs(clinic_id):
    tt =  twitter_api.statuses.user_timeline(screen_name=clinic_id)
    for msg in tt:
        print json.dumps(msg['text'], indent=1)

# get_msgs('LMCSaskatoon')

