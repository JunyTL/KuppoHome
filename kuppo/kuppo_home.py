from flask import (
	Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

#from flaskr.auth import login_required
from kuppo.db import get_db

bp = Blueprint('home', __name__)		# home page

@bp.route('/')
def home():
	db = get_db()
	
	return render_template('home.html')

	