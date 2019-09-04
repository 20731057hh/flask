from flask import Flask
from flask.ext.sqlalchemy　import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskr.config')
db = SQLAlchemy(app)

import flaskr.views
