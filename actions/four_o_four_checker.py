# -*- coding: utf8 -*-

from action import *
import re, urllib2

class FourOFourChecker(Action):

	def recognize(self, data):
		if not self.security.checkSecurity(data):
			return False
			
		# @see https://gist.github.com/uogbuji/705383
		regex = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

		m = re.findall(regex, data.msg)
		if not m:
			return False
		url = m[0][0]

		print url
		try:
			req = urllib2.Request(url, headers={'User-Agent' : "Tonton bot"}) 
			con = urllib2.urlopen(req)
			con.read()
			#urllib2.urlopen(url).read()
			return False
		except urllib2.HTTPError, e:
			self.data = "%s me retourne une erreur %s" % (url, e.code)
		except urllib2.URLError, e:
			self.data = "je n'ai pas pu attendre l'url %s : %s" % (url, e.reason)

		return True

	def execute(self):
		return self.data
