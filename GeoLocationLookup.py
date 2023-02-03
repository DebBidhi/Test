#geojason.py
import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    place_id = js['results'][0]['place_id']
    print(location)
    print('the Place_id is:',place_id)
'''
The script imports the necessary libraries (urllib, json, and ssl) and sets up a variable for a Google Places API key. If no key is provided, it uses a default key.
The script then prompts the user for an address and creates a URL with the address and API key (if provided) to send a request to the Google Geocoding API.
The API response, in JSON format, is parsed and the latitude, longitude, location, and place_id of the address are extracted and printed out. the jason format is as follows:
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "Kushtia",
                    "short_name": "Kushtia",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Nadia",
                    "short_name": "Nadia",
                    "types": [
                        "administrative_area_level_3",
                        "political"
                    ]
                },
                {
                    "long_name": "Presidency Division",
                    "short_name": "Presidency Division",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "West Bengal",
                    "short_name": "WB",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "India",
                    "short_name": "IN",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "741160",
                    "short_name": "741160",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "Kushtia, West Bengal 741160, India",
            "geometry": {
                "bounds": {
                    "northeast": {
                        "lat": 23.7185199,
                        "lng": 88.47787009999999
                    },
                    "southwest": {
                        "lat": 23.69715,
                        "lng": 88.45345
                    }
                },
                "location": {
                    "lat": 23.705107,
                    "lng": 88.46218909999999
                },
                "location_type": "APPROXIMATE",
                "viewport": {
                    "northeast": {
                        "lat": 23.7185199,
                        "lng": 88.47787009999999
                    },
                    "southwest": {
                        "lat": 23.69715,
                        "lng": 88.45345
                    }
                }
            },
            "place_id": "ChIJ44Zg9J0V-TkR4sYF9pmXpUM",
            "types": [
                "locality",
                "political"
            ]
        }
    ],
    "status": "OK"
}
''' 
    



