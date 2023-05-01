import requests

def GetHtml(config):
	r = requests.get(config.url, headers = config.headers)
	r.encoding = 'utf-8'
	config.html = r.text
	return config

