import requests

def Get_Access_Token(hfclientid, hfsecret, code, proxyurl):
	url = f'https://hackforums.net/api/v2/authorize'
	querystring = {
		"grant_type":"authorization_code",
		"client_id":hfclientid,
		"client_secret":hfsecret,
		"code":code
	}
	payload = ""
	headers = {}

	
	try:
		if proxyurl:
			proxy = {'http': proxyurl, 'https':proxyurl}
			r = requests.post(url, data=payload, headers=headers, params=querystring, proxies=proxy)
		else:
			r = requests.post(url, data=payload, headers=headers, params=querystring)
		return r.json()['access_token'], r.json()['uid']
	except:
		return False, False