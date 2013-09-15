# -*- coding: utf8 -*-

from actions.about import *
from actions.four_o_four_checker import *
from actions.google import *
from actions.nsfw_gag import *
from actions.uptime import *
from actions.ping import *
from actions.youtube import *
from actions.quit import *
from actions.help import *
from security import *

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
		youtube = Youtube(application, 'youtube', 'Nom / Auteur / Durée de la vidéo', security)
		actionList.append(youtube)

		security = Security()
		security.addToWhiteList('tonton')
		google = Google(application, '!google', '@todo', security)
		actionList.append(google)

		security = Security()
		nsfw = NSFWGag(application, 'nsfw_gag', 'Signale les posts 9gag NSFW', security)
		actionList.append(nsfw)
		
		security = Security()
		uptime = Uptime(application, '!uptime', 'Retourne l\'uptime de ce bot', security)
		actionList.append(uptime)

		security = Security()
		ping = Ping(application, '!ping', 'pong', security)
		actionList.append(ping)

		security = Security()
		help = Help(application, '!help', 'Affiche la liste des commandes', security)
		actionList.append(help)

		security = Security()
		security.addToWhiteList('tonton')
		quit = Quit(application, '!quit', 'Quitter', security)
		actionList.append(quit)
		
		#
		# Reads xml config files
		#
		
		
		return actionList
