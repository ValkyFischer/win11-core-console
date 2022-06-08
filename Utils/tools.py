"""https://valky.dev/"""

import configparser
import os
from time import time
from datetime import datetime


def readConfig(ini: str) -> dict:
	""" Read config, check for errors and store values

	:param ini: Path to config_wa_gw.ini
	:return: Config as dict
	"""
	# Read config
	config = configparser.ConfigParser()
	config.read(ini)
	return config


def performance(stage: str, time: datetime = None):
	"""

	:param stage: Choose start or stop
	:param time: Add start time when stopping
	:return: Time as datetime or in Seconds
	"""
	match stage:
		case "start":
			return datetime.now()
		case "end":
			return (datetime.now() - time).total_seconds()


def createLog(msg: str, debug: bool):
	log_t = datetime.now().strftime("%Y/%m/%d %H:%M:%S.%f")[:-3]
	log = f"[{log_t}] {msg}"
	if debug: print(log)
	writeLog(log)


def writeLog(log: str):
	with open("./logs/Win11CC.log", "a") as logfile:
		logfile.write(log+"\n")


def recycleLog():
	os.rename(f"./logs/Win11CC.log", f"./logs/Win11CC.{int(time())}.log")
