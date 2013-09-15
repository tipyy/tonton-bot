# -*- coding: utf8 -*-

from security import *
import actions

class ActionListFactory(object):

	def create(self, application):
		actionList = []

		security = Security()		
		about = actions.About(application, '!about', 'Affiche les crédits', security)
		actionList.append(about)

		security = Security()
		fourofour = actions.FourOFourChecker(application, 'fourofour', 'Renvoi un message si une url renvoit une erreur 404', security)
		actionList.append(fourofour)

		security = Security()
		youtube = actions.Youtube(application, 'youtube', 'Nom / Auteur / Durée de la vidéo', security)
		actionList.append(youtube)

		security = Security()
		nsfw = actions.NSFWGag(application, 'nsfw_gag', 'Signale les posts 9gag NSFW', security)
		actionList.append(nsfw)
		
		security = Security()
		uptime = actions.Uptime(application, '!uptime', 'Retourne l\'uptime de ce bot', security)
		actionList.append(uptime)

		security = Security()
		ping = actions.Ping(application, '!ping', 'pong', security)
		actionList.append(ping)

		security = Security()
		help = actions.Help(application, '!help', 'Affiche la liste des commandes', security)
		actionList.append(help)

		security = Security()
		security.addToWhiteList('tonton')
		quit = actions.Quit(application, '!quit', 'Quitter', security)
		actionList.append(quit)
		
		#
		# Reads xml config files
		#
		
		
		return actionList
