from __future__ import print_function
# これだとエラーになるので下記に修正
# from flask.ext.script import Manager
from flask_script import Manager
from flaskr import app, db

manager = Manager(app)

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
