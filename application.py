from mongoengine import *
from flask import Flask, render_template, request
from flights import fetch_flights, fetch_nearest_airports

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/junction'

connect('junction')

@app.route('/', methods=['GET'])
def questions():
    return render_template('questions.html')

@app.route('/experiences', methods=['GET'])
def experiences():
    return render_template('experiences.html')

@app.route('/flights', methods=['GET'])
def flights():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    nearest_airports = fetch_nearest_airports(latitude, longitude)
    return render_template('flights.html')

if __name__ == '__main__':
    app.run()
