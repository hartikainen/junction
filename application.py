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
    origin = request.args.get('origin').split(" ")
    destination = request.args.get('destination').split(" ")
    departure_date = request.args.get('departure')
    print departure_date

    nearest_airport_origin = fetch_nearest_airports(float(origin[0]),
                                                    float(origin[1]))

    nearest_airport_destination = fetch_nearest_airports(float(destination[0]),
                                                         float(destination[1]))

    flight_data = fetch_flights(nearest_airport_origin,
                                nearest_airport_destination,
                                departure_date)

    return flight_data#render_template('flights.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
