# -*- coding: utf8 -*-

from actions.about import *
from actions.clean_url import *
from actions.four_o_four_checker import *
from actions.nsfw_gag import *
from actions.uptime import *
from actions.ping import *
from actions.quit import *
from security import *

# todo use xml or json
class ActionListFactory(object):

	def create(self, application):
		actionList = []

		security = Security()		
		about = About(application, '!about', 'Affiche les crédits', security)
		actionList.append(about)

		security = Security()
		fourofour = FourOFourChecker(application, 'fourofour', 'Renvoi un message si une url renvoit une erreur 404', security)
		actionList.append(fourofour)
		
		security = Security()
		clean_url = Youtube(application, 'youtube_clean_url', 'Nettoie automatiquement les url youtube', security)
		actionList.append(clean_url)

		security = Security()
		nsfw = NSFWGag(application, 'nsfw_gag', 'Post 9gag nécessitant de s authentifier (WorkInProgress)', security)
		actionList.append(nsfw)
		
		security = Security()
		uptime = Uptime(application, '!uptime', 'Retourne l\'uptime de ce bot', security)
		actionList.append(uptime)

		security = Security()
		ping = Ping(application, '!ping', 'Renvoi un pong', security)
		actionList.append(ping)
		
		security = Security()
		security.addToWhiteList('tonton')
		quit = Quit(application, '!quit', 'Quitter', security)
		actionList.append(quit)
		
		return actionList
