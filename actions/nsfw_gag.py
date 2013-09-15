# -*- coding: utf8 -*-

from bs4 import BeautifulSoup
from action import *
import re, urllib, urllib2, cookielib

class NSFWGag(Action):
	def recognize(self, data):
		if not self.security.checkSecurity(data):
			return False

		regex = '((http://|https://)*(www.)*9gag.com[a-zA-Z/0-9?=]*)'
		m = re.findall(regex, data.msg)
		if not m:
			return False

		try:		
			url = urllib2.urlopen('%s' % m[0][0]).read()
		except urllib2.HTTPError, e:
			return False
		except urllib2.URLError, e:
			return False

		soup = BeautifulSoup(url)
		if soup.find('p', {'class': 'form-message error '}) is not None:
			self.data = 'Ce post a été supprimé'
			return True

		if soup.find('div', {'class': 'nsfw-post'}) is not None:
			self.data = 'Ce post de 9gag nécessite de s\'identidier'

			return True

		return False

	def execute(self, data):
		return self.data
