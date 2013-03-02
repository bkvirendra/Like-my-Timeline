import requests
import datetime
import time

from random import randrange

TOKEN = "" # add your access token here, with publish_stream permission

def main():
	todays_start_unixtimestamp = int(time.mktime((datetime.datetime(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 0, 0, 0)).timetuple()))
	print "fetching the posts.."
	data = requests.get("https://graph.facebook.com/me/feed?since=" + str(todays_start_unixtimestamp) + "&limit=200&access_token=" + TOKEN)
	posts_ids = []
	breakit = lambda x: x.split("_")[1]
	for k in data.json['data']:
		try:
			if 'happy' in k.get("message").lower():
				posts_ids.append(str(breakit(k.get('id'))))
		except Exception, e:
			print e
	comments = ["Thanks :)", "thank you :)", "thank you", "thanks"]
	payload = {}
	for each_id in posts_ids:
		# like the post
		print "Posting the like..."
		like_url = "https://graph.facebook.com/" + each_id + "/likes?access_token=" + TOKEN
		resp = requests.post(like_url, data=payload)
		print "Like posted!"
		print resp.text
		# comment on the post
		"""
		print "Posting the comment..."
		comment_url = "https://graph.facebook.com/" + each_id + "/comments?access_token=" + TOKEN
		comment = requests.post(comment_url, data={'message':comments[randrange(4)]})
		print "Comment posted..."
		print comment.text
		"""
	print "Done..!"
	return

if __name__ == '__main__':
	main()
