import os
from flask import Flask

def create_app(test_config = None):
	app = Flask(__name__, instance_relative_config = True)		#create app
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE = os.path.join(app.instance_path, 'kuppo.sqlite')
	)

	if test_config is None :
		app.config.from_pyfile('config.py', silent = True)
	else :
		app.config.from_mapping(test_config)

	try:
		os.makedirs(app.instance_path)
	except OSError :
		pass

	from . import db 
	db.init_app(app)

	from . import kuppo_home
	app.register_blueprint(kuppo_home.bp)

	from . import member
	app.register_blueprint(member.bp)
	
	app.add_url_rule('/', endpoint='home')

	return app

app = create_app()