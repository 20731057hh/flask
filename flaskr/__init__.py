from flask import Flask
# これだとエラーになるので下記に修正
# from flask.ext.sqlalchemy import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('flaskr.config')
db = SQLAlchemy(app)

import flaskr.views
