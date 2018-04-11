#	project/__init__.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_session import Session
from tempfile import mkdtemp

app	= Flask(__name__)
app.config.from_pyfile('_config.py')
# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

from project.start.views import start_blueprint
from project.users.views import users_blueprint
from project.tasks.views import tasks_blueprint

#	register	our	blueprints
app.register_blueprint(start_blueprint)
app.register_blueprint(users_blueprint)
app.register_blueprint(tasks_blueprint)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),	404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500