import notify2
import feedparser

import os
import time


def parse_feed():
	f = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml") 
	#returns parsed data in form of dictionary
	ICON_PATH = os.getcwd() + '/news_icon.ico' 
	# set icon for the notification
	notify2.init('Desktop News Notifier') 
	# initializing dbus connection
	
	# Loop through parsed data to get relevant info for notification
	for news_item in f['items']:
		n = notify2.Notification(news_item['title'],news_item['summary'],icon = ICON_PATH)

	n.set_urgency(notify2.URGENCY_NORMAL)
	n.show()
	n.set_timeout(15000) #notification stays for 15 seconds
	time.sleep(100)     #time difference between each notification




if __name__ == '__main__':
	parse_feed()
