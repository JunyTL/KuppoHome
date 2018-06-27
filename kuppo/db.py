import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext			# command line interface

def init_db():
	db = get_db()
	with current_app.open_resource('schema.sql') as f:		# create db
		db.executescript(f.read().decode('utf-8'))			# read database schema

@click.command('init-db')				# execute when entered command
@with_appcontext
def init_db_command():
	init_db()
	click.echo('Initialized the database')	# after called init_db func.

def init_app(app):
	app.teardown_appcontext(close_db)
	app.cli.add_command(init_db_command)	# register command. necessary

def get_db():
	if 'db' not in g :					# g is associated with application context
		g.db = sqlite3.connect(
			current_app.config['DATABASE'],
			detect_types = sqlite3.PARSE_DECLTYPES
		)
		g.db.row_factory = sqlite3.Row

	return g.db

#@app.teardown_appcontext				# whenever execute if appcontext get request
def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()
