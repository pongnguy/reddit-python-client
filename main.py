import requests
import json

# note that CLIENT_ID refers to 'personal use script' and SECRET_TOKEN to 'token'
CLIENT_ID = "0O2YmTN95QrRKdrXFjyUBg"
SECRET_TOKEN = "xiri924wbKUA799SAfC_KuuX8mDXqA"

auth = requests.auth.HTTPBasicAuth(CLIENT_ID, SECRET_TOKEN)

# here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': 'pongnguy',
        'password': 'Dd52385238'}

# setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': 'MyBot/0.0.1'}

# send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# while the token is valid (~2 hours) we just add headers=headers to our requests
res = requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

print(res.json())

#%%
SUBREDDIT="wallstreetbets"
res = requests.get("https://oauth.reddit.com/r/{0}/hot".format(SUBREDDIT),
                   headers=headers)
with open('responses/{0}/hot.json'.format(SUBREDDIT), 'w', encoding='utf-8') as jsonFile:
    jsonFile.write(json.dumps(res.json()))
    #jsonFile.write(json.dumps(res.json()))
    print(res.json())  # let's see what we get


