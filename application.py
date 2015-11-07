from mongoengine import *
from flask import Flask, render_template
from flights import fetch_flights

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/junction'

connect('junction')

@app.route('/', methods=['GET'])
def questions():
    return render_template('questions.html');

@app.route('/experiences', methods=['GET'])
def experiences():
    return render_template('experiences.html');

if __name__ == '__main__':
    app.run()
