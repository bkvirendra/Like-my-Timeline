import requests, json, urllib2

token = "" # add you're access token here, with publish_stream permission

def main():
	url = "https://graph.facebook.com/me/feed?access_token=" + token
	data = urllib2.urlopen(url)
	js = json.loads(data.read())
	likes_id = []
	breakit = lambda x: x.split("_")[1]
	for k in js['data']:
		likes_id.append(k['id'])
	payload = {}
	for each_id in likes_id:
		like_url = "https://graph.facebook.com/" + breakit(each_id) + "/likes?access_token=" + token
		resp = requests.post(like_url, data=payload)
		print resp.text

if __name__ == '__main__':
	main()