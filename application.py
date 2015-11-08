from flask import Flask, render_template, request
from flights import fetch_flights, fetch_nearest_airports
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger

import os

db_url = ''

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

Base = declarative_base()

class Experience(Base):
    __tablename__ = 'experiences'
    key = db.Column('key_column',db.BigInteger, primary_key=True)
    experience = db.Column('experience', db.String) 
    place = db.Column('place', db.String)
    country = db.Column('country', db.String)
    image = db.Column('image', db.String)
    description = db.Column('description', db.String)
    nature_urban = db.Column('nature_urban', db.String)
    adventure_chill = db.Column('adventure_chill', db.String)
    airbnb = db.Column('airbnb', db.String)
    airbnb_price = db.Column('airbnb_price', db.Integer)
    experience_link = db.Column('experience_link', db.String)
    experience_price = db.Column('experience_price', db.Integer)

for instance in db.session.query(Experience):
    print instance

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
