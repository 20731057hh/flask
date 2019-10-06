from flask import Flask, render_template, jsonify
from api import api_bp
from models import get_all, init_db, insert
from random import randint

app = Flask(__name__,
            static_folder='../frontend/dist/static',
            template_folder='../frontend/dist')
app.config['SQLALCHEMY_DATBASE_URI'] = 'sqlite:///myspa.db'
app.register_blueprint(api_bp)

@app.route('/api/random')
def random_number():
    response = {
        'randomNumber':randint(1,100)
    }
    return jsonify(response)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
        if not get_all():
            insert('foo', 'This is foo')
            insert('bar', 'This is bar')
    app.run()
