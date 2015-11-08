import unicodedata
import requests
import json

QPX_KEY = "AIzaSyCGG7RIlC4tKUe_lRPEnPLHv4_wbbJk8P8"
AERO_KEY = "e6f866816ab0b233fc098adeabab8cf8"
R = False

def fetch_flights(origin=False, destination=False, date="2015-11-10"):
    print origin
    print destination
    print date
    r = R
    params = {"key": QPX_KEY}
    request_data = {
        "request": {
            "passengers": {
                "kind": "qpxexpress#passengerCounts",
                "adultCount": 1,
                "childCount": 0,
                "infantInLapCount": 0,
                "infantInSeatCount": 0,
                "seniorCount": 0
            },
            "slice": [
                {
                    "kind": "qpxexpress#sliceInput",
                    "origin": origin,
                    "destination": destination,
                    "date": date,
                    "maxStops": 1,
                    "maxConnectionDuration": 4320,
                    "preferredCabin": "COACH",
                    "permittedDepartureTime": {
                        "kind": "qpxexpress#timeOfDayRange",
                        "earliestTime": "00:00",
                        "latestTime": "23:59"
                    },
                }
            ],
            "maxPrice": "USD10000.0",
            "refundable": False,
            "solutions": 500
        }
    }

    if not r:
        r = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search',
                          json = request_data, params = params)

    response = json.loads(r.text)
    print r.text[0:1000]
    return r.text

def fetch_nearest_airports(latitude, longitude):
    url = "https://airport.api.aero/airport/nearest/%.15f/%.15f" % (float(latitude), float(longitude))
    params = {
        "maxAirports": 1,
        "user_key": AERO_KEY
    }
    r = requests.get(url, params = params)
    response_str = r.text[len("callback("):-1]
    print response_str
    response = json.loads(response_str)
    print response['airports']
    for airport in response['airports']:
        print airport['code']

    airport_code = response['airports'][0]['code']

    return airport_code
