from mongoengine import *
from flask import Flask, render_template
from flights import fetch_flights

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/junction'

connect('junction')

@app.route('/', methods=['GET'])
def main_page():
    #fetch_flights()
    return render_template('main.html');

if __name__ == '__main__':
    app.run()
