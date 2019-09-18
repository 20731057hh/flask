from flask import Flask, render_templste

app = Flask(__name__, static_folder='../fronted/dist/static', template_folder='../fronted/dist')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
