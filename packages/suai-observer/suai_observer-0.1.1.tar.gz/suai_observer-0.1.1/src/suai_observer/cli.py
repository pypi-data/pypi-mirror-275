import sys
import toml
import json

from suai_observer.config import Config
from suai_observer.session import SuaiSession

def config_from_file(filename: str) -> Config:
	content = None
	with open(filename, 'r') as f:
		content = toml.load(f)

	timeout = content["timeout"]
	assert type(timeout) == int

	cookiefile = content["cookiefile"]
	assert type(cookiefile) == str

	username = content["username"]
	assert type(username) == str

	password = content["password"]
	assert type(password) == str

	return Config(timeout, cookiefile, username, password)

def main():
	configfile = sys.argv[1]
	config = config_from_file(configfile)

	session = SuaiSession(config.timeout, config.cookiefile, config.username, config.password)

	comma = ''
	sys.stdout.write('[')
	for report in session.reports():
		sys.stdout.write(comma)

		json_report = {
			"task": report.task,
			"professor": report.professor,
			"status": report.status,
			"score": report.score,
			"date": report.date,
		}
		json.dump(json_report, sys.stdout, ensure_ascii=False)

		comma = ','
	sys.stdout.write(']')
