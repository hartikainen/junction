import requests

def fetch_flights(origin=False, destination=False):
    params = {"key": APP_KEY}
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
                    "origin": "HEL",
                    "destination": "SFO",
                    "date": "2015-11-08",
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

    r = requests.post('https://www.googleapis.com/qpxExpress/v1/trips/search',
                      json = request_data, params = params)
    print r.url
    print r.text
    return
