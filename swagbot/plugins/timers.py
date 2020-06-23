from dateutil.relativedelta import relativedelta
from pprint import pprint, pformat
from swagbot.core import BasePlugin
import argparse
import datetime
import re
import swagbot.request as request
import swagbot.timers_database as db
import swagbot.utils as utils
import sys
import time

class Plugin(BasePlugin):
	def __init__(self, bot):
		self.methods = self.__setup_methods()
		BasePlugin.__init__(self, bot)

	def timer(self, command=None):
		if command:
			title = command.command_args
			if title:
				timer = db.timer(title=title)
				if timer:
					now = int(time.time())					
					if now < timer["expires"]:
						starts = datetime.datetime.fromtimestamp(now)
						ends = datetime.datetime.fromtimestamp(timer["expires"])
						diff = relativedelta(ends, starts)
						duration = []
						if diff.years: duration.append("{} years".format(diff.years))
						if diff.months: duration.append("{} months".format(diff.months))
						if diff.days: duration.append("{} days".format(diff.days))
						if diff.hours: duration.append("{} hours".format(diff.hours))
						if diff.minutes: duration.append("{} minutes".format(diff.minutes))
						if diff.seconds: duration.append("{} seconds".format(diff.seconds))

						utils.make_success(command, content="{} until {}!".format(" ".join(duration), timer["description"]))
					else:
						utils.make_success(command, content="Timer \"{}\" with the description\"{}\" has expired.".format(title, timer["description"]))
				else:
					utils.make_error(command, content="Timer \"{}\" not found.".format(title))
			else:
				utils.make_error(command, content=["No title specified.", "Usage: {}".format(command.command["usage"])])	
		else:
			utils.make_error(command, content="An unknown error has occurred.")

	def timers(self, command=None):
		if command:
			timers = db.timers()
			if len(timers) > 0:
				utils.make_success(command, content="Available timers: {}".format(", ".join(timers)))
			else:
				utils.make_success(command, content="No timers found.")
		else:
			utils.make_error(command, content="An unknown error has occurred.")

	def timeradd(self, command=None):
		# Verify existence here
		if command:
			sys.argv = command.argv
			parser = argparse.ArgumentParser(description=command.command["usage"])
			parser.add_argument("-t", "--title", help="The timer's title.", required=True)
			parser.add_argument("-d", "--description", help="The timer's description.", required=True)
			parser.add_argument("-e", "--expires", help="The timer's expiration date in the format YYYY-MM-DD.", required=True)
			try:
				args = parser.parse_args()
			except:
				utils.make_error(command, content=["Invalid input received.", "Usage: {}".format(command.command["usage"])])
				return

			expires_timestamp = None
			now = int(time.time())
			if re.search("\d\d\d\d-\d\d-\d\d", args.expires):
				try:
					expires_timestamp = int(time.mktime(datetime.datetime.strptime(args.expires, "%Y-%m-%d").timetuple()))
				except:
					utils.make_error(command, content="Invalid date: {}".format(expires))
					return
				if expires_timestamp < now:
					utils.make_error(command, content="Expiration cannot be in the past.")
					return

				db.timeradd(title=args.title,description=args.description,expires=expires_timestamp)
				utils.make_success(command, content="Successfully added the timer \"{}\".".format(args.title))
		else:
			utils.make_error(command, content="An unknown error has occurred.")

	def timerdel(self, command=None):
		if command:
			sys.argv = command.argv
			parser = argparse.ArgumentParser(description=command.command["usage"])
			parser.add_argument("-t", "--title", help="The timer's title.", required=True)
			try:
				args = parser.parse_args()
			except:
				utils.make_error(command, content=["Invalid input received.", "Usage: {}".format(command.command["usage"])])
				return

			timer = db.timer(title=args.title)
			if timer:
				db.timerdel(title=args.title)
				utils.make_success(command, content="Successfully deleted the timer \"{}\".".format(args.title))
			else:
				utils.make_success(command, content="Timer \"{}\" doesn't exist. Nothing to do.".format(args.title))
		else:
			utils.make_error(command, content="An unknown error has occurred.")

	def __setup_methods(self):
		return {
			"timer": {
				"usage": "timer <title> -- Show how long until a given timer.",
				"level": 0,
				"type": "all",
				"can_be_disabled": 1,
				"hidden": 0,
				"monospace": 0
			},
			"timers": {
				"usage": "timers -- List all of the timers in the timer table.",
				"level": 0,
				"type": "all",
				"can_be_disabled": 1,
				"hidden": 0,
				"monospace": 0
			},
			"timeradd": {
				#"usage": "timeradd <title>|<description>|<YYYY-MM-DD> -- Add a new timer.",
				"usage": "timeradd -t <title> -d <description> -e <YYYY-MM-DD> -- Add a new timer.",
				"level": 0,
				"type": "all",
				"can_be_disabled": 1,
				"hidden": 0,
				"monospace": 0
			},
			"timerdel": {
				"usage": "timerdel -t <title> -- Delete an existing timer.",
				"level": 0,
				"type": "all",
				"can_be_disabled": 1,
				"hidden": 0,
				"monospace": 0
			},
		}

	def __ts2human(self, ts):
		if ts == -1:
			return "unknown"
		else:
			return (datetime.datetime.fromtimestamp( int(ts)).strftime("%Y-%m-%d %H:%M:%S"))
