import config
import requests

# Here we pass our client id and secret token
auth = requests.auth.HTTPBasicAuth(config.client_id, config.secret_token)

# Here we pass our login method (password), username, and password
data = {'grant_type': 'password',
        'username': config.username,
        'password': config.password}

# Setup our header info, which gives reddit a brief description of our app
headers = {'User-Agent': config.botname + 'Bot/0.0.1'}

# Send our request for an OAuth token
res = requests.post('https://www.reddit.com/api/v1/access_token',
                    auth=auth, data=data, headers=headers)

# Convert response to JSON and pull access_token value
TOKEN = res.json()['access_token']

# Add authorization to our headers dictionary
headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

# While the token is valid (~2 hours) we just add headers=headers to our requests
requests.get('https://oauth.reddit.com/api/v1/me', headers=headers)

# Pull results
res = requests.get("https://oauth.reddit.com/r/ottawa/hot",
                   headers=headers,
                   params={'limit': '100'})

for post in res.json()['data']['children']:
    print(post['data']['subreddit'])
    print(post['data']['title'])
    print(post['data']['selftext'])
    print(post['data']['upvote_ratio'])
    print(post['data']['ups'])
    print(post['data']['downs'])
    print(post['data']['score'])