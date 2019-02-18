import os
import requests
import pprint
"""client access token is kinda a bullshit way to do this, should probably
use actual authorization"""

token = os.environ['GENIUS_TOKEN']
url = 'https://api.genius.com'

payload = {
        'access_token':token
        }


response = requests.get(url + '/search?q=Kanye', data=payload)

pprint.pprint(response.text)


