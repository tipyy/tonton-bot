# -*- coding: utf8 -*-

from action import *
import re, urllib2, json

class Youtube(Action):
	def recognize(self, data):

		regex = '(http(s)?://)?(www.)?(youtu\.be\/|youtube\.com\/(watch\?(.*&)?v=|(embed|v)\/))([^\?\&"\'\ >]+)'
		
		m = re.findall(regex, data.msg)

		if m:
			self.data = m
			self.application.logger.info("Youtube url detected %s" % m)
			return True
		return False

	def execute(self, data):
		api_url = 'https://gdata.youtube.com/feeds/api/videos/%s?v=2&alt=jsonc' % self.data[0][7]
		json_encoded = ""
		
		try:
			req = urllib2.Request(api_url, headers={'User-Agent' : "Tonton bot"}) 
			con = urllib2.urlopen(req)
			json_encoded = con.read()
					
			encoded_data = json.loads(json_encoded)
			self.application.logger.debug(encoded_data)
		except urllib2.HTTPError, e:
			self.application.logger.debug("youtube error")

		d = encoded_data['data']['duration']
		import datetime
		duration = str(datetime.timedelta(seconds=d))
		title = "%s / %s / %s" % (encoded_data['data']['uploader'],encoded_data['data']['title'],duration)
		import unicodedata
		
		return unicodedata.normalize('NFKD', title).encode('utf8','ignore')
