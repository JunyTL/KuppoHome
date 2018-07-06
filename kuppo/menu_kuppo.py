from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from flaskr.auth import login_required
from kuppo.db import get_db

bp = Blueprint("menu_kuppo", __name__, url_prefix="/menu_kuppo")

def get_user():
	return

@bp.route("/intro")
def intro():
	return render_template("menu_kuppo/intro.html");

@bp.route("/notice")
def notice():
	db = get_db()

	#notices = db.execute(
	#	'SELECT n.id, title, body, created, author_id, username'
	#	' FROM notice n JOIN user u ON n.author_id = u.id'
	#	' ORDER BY created DESC'
	#	).fetchall()
	return render_template("menu_kuppo/notice.html");

@bp.route("/calendar")
def calendar():
	db = get_db()
	return render_template("menu_kuppo/calendar.html");

@bp.route("/suggestion", methods=('GET', 'POST'))
#@login_required
def suggestion():
	db = get_db()

	# add 
	if request.method == 'POST' :
		username = request.form['username']
		title = request.form['title']
		category = request.form['category']
		body = request.form['context']

	return render_template("menu_kuppo/suggestion.html");