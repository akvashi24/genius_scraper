import os
import requests
import pprint
import json
"""client access token is kinda a bullshit way to do this, should probably
use actual authorization"""

token = os.environ['GENIUS_TOKEN']
url = 'https://api.genius.com'

payload = {
        'access_token':token
        }


response = requests.get(url + '/songs/70324', data=payload )

json_obj = json.loads(response.text)

for k in json_obj['response']['song']:
    print(k)
