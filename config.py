#config.py
import os
import sys
#sys.path.insert(0, '/app/site-packages')
from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8082))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

#Gunicorn config
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()


