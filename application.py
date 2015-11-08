#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, jsonify
from flights import fetch_flights, fetch_nearest_airports
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, BigInteger

import os
import json

db_url = ''

app = Flask(__name__, static_folder='static', static_url_path='/static')
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = db_url
db = SQLAlchemy(app)

Base = declarative_base()

class Experience(db.Model):
    __tablename__ = 'experiences'
    key = db.Column('key_column',db.BigInteger, primary_key=True)
    experience = db.Column('experience', db.String) 
    place = db.Column('place', db.String)
    country = db.Column('country', db.String)
    image = db.Column('image', db.String)
    description = db.Column('description', db.String)
    nature_urban = db.Column('nature_urban', db.String)
    adventure_chill = db.Column('adventure_chill', db.String)
    warm_cold = db.Column('warm_cold', db.String)
    airbnb = db.Column('airbnb', db.String)
    airbnb_price = db.Column('airbnb_price', db.Integer)
    experience_link = db.Column('experience_link', db.String)
    experience_price = db.Column('experience_price', db.Integer)

    def getJSON(self):
        return "{'key':"+str(self.key)+"," + \
                "'experience':'" + self.experience +"',"+ \
                "'place':'" + self.place +"',"+ \
                "'country':'" + self.country +"',"+ \
                "'image':'" + self.image +"',"+ \
                "'description':'" + self.description +"',"+ \
                "'nature_urban':'" + self.nature_urban +"',"+ \
                "'adventure_chill':'" + self.adventure_chill +"',"+ \
                "'warm_cold':'" + self.warm_cold +"',"+ \
                "'airbnb':'" + self.airbnb +"',"+ \
                "'airbnb_price':" + str(self.airbnb_price) +","+ \
                "'experience_link':'" + self.experience_link +"',"+ \
                "'experience_price:" + str(self.experience_price) + \
                "}"


@app.route('/', methods=['GET'])
def questions():
    return render_template('questions.html')

@app.route('/experiences', methods=['GET'])
def experiences():
    query = request.args.get('query')
    try:
        resArray = []
        qarr = query.split();
        dbq = Experience.query.filter_by(nature_urban=qarr[0],adventure_chill=qarr[1], warm_cold=qarr[2])
        for it in dbq:
            resArray.append(it.getJSON().encode('utf-8'))

        return json.dumps(resArray)

    except:
        return "[{'key':-1}]"

@app.route('/flights', methods=['GET'])
def flights():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    nearest_airports = fetch_nearest_airports(latitude, longitude)
    return render_template('flights.html')

if __name__ == '__main__':
    app.run()
