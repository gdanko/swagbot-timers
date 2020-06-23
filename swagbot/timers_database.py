import os
import sqlite3

PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

def timer(title=None):
	select = "SELECT * FROM timers WHERE title='{}'".format(title)
	cursor.execute(select)
	result = cursor.fetchone()
	return result if result else None

def timers():
	timers = []
	select = "SELECT title FROM timers"
	res = cursor.execute(select)
	for row in res:
		timers.append(row["title"])
	return timers

def timeradd(title=None,description=None,expires=None):
	insert = "INSERT INTO timers (title,description,expires,expired) VALUES (?,?,?,?)"
	cursor.execute(insert, (
		title,
		description,
		expires,
		0
	))
	conn.commit()

def timerdel(title=None):
	delete = "DELETE FROM timers WHERE title='{}'".format(title)
	cursor.execute(delete)
	conn.commit()

def _dict_factory(cursor, row):
	d = {}
	for idx,col in enumerate(cursor.description):
		d[col[0]] = row[idx]
	return d

dbfile = "{}/data/timers.db".format(PACKAGE_ROOT)
conn = sqlite3.connect(dbfile, check_same_thread=False)
conn.row_factory = _dict_factory
cursor = conn.cursor()