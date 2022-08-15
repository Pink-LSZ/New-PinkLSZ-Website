import requests, os

def get_discord_access_token(discordclient, discordsecret, redirecturi, code):
	API_ENDPOINT = 'https://discord.com/api/'
	data = {
		'client_id': discordclient,
		'client_secret': discordsecret,
		'grant_type': 'authorization_code',
		'code': code,
		'redirect_uri': redirecturi
	}
	headers = {
		'Content-Type': 'application/x-www-form-urlencoded'
	}
	r = requests.post('https://discord.com/api/oauth2/token', data=data, headers=headers)
	return r.json()['access_token']

def get_discord_user(access_token):
	url = 'https://discord.com/api/users/@me'
	headers = {
	    'Authorization': f'Bearer {access_token}'
	}
	
	r = requests.get(url, headers=headers)
	
	return r.json()