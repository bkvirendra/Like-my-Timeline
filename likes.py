import requests, json, urllib2

token = "AAACEdEose0cBAEkq5JVqZACK450OLAEpk5CmuwZCNZAw1rPnXgwlZC5g1HXzGDtUovgmly7Rrakl5LrytcUprnfbi5tFmfe0mmmXlajU7jyZAcQo0c4hq"

def main():
	url = "https://graph.facebook.com/me/feed?since=1353609000&access_token=" + token
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