import urllib
import json
import re
import math
import googlemaps
from datetime import datetime

import barrios
import data

app_key = 'AIzaSyBv0RCGswuYS5g52SBUpMvZKCElkfzPdtA'
# gmaps = googlemaps.Client(key=app_key)

nombres_barrios = ['teusaquillo', 'la florida occidental', 'samper mendoza', 'estacion central', 'paloquemao',
               'quinta paredes']

barrios.get_barrios_data(nombres_barrios)

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'https://maps.googleapis.com/maps/api/directions/json?origin=Universidad+nacional+de+colombia,Bogota&destination=Centro+comercial+calima,Bogota&alternatives=true&key='

url = serviceurl+app_key

js = data.get_data(url)

durations = list()

print(json.dumps(js['routes'][0], indent=4))
# for route in js['routes']:
#     print(route['summary'])
#     for leg in route['legs']:
#         durations.append(re.findall('\d+', leg['duration']['text'] )[0])
#         for step in leg['steps']:
#             print ('origin is' + json.dumps(step['start_location'])+ 'end is= ' +json.dumps(step['end_location']))



# # math.acos(math.sin(lat1)* math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon1-lon2)) * 6371


# print(durations)


# print(json.dumps(js['routes'][0]['legs'][0]['distance'], indent=4))
