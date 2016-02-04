#!/usr/bin/env python
import os
import sys

# settings
RUNSERVER_ENDPOINT = "0.0.0.0:8000"
RUNSERVER_OPTIONS = ["--insecure"]

# customize default command settings
def runserver_defaults():
	if sys.argv[1] == 'runserver':
		sys.argv.insert(2, RUNSERVER_ENDPOINT)
		sys.argv.extend(RUNSERVER_OPTIONS)
		print "Using custom default server options: {} {}!".format(RUNSERVER_ENDPOINT, RUNSERVER_OPTIONS)

# main
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
    if os.environ.get('RUN_MAIN'):
		runserver_defaults()
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
