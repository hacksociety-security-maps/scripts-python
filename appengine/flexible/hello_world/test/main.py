import json

import barrios
import ruta

app_key = 'AIzaSyBv0RCGswuYS5g52SBUpMvZKCElkfzPdtA'
# gmaps = googlemaps.Client(key=app_key)

nombres_barrios = ['teusaquillo', 'la florida occidental', 'samper mendoza', 'estacion central', 'paloquemao',
               'quinta paredes']

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'https://maps.googleapis.com/maps/api/directions/json?origin=Universidad+nacional+de+colombia,Bogota&destination=Centro+comercial+calima,Bogota&alternatives=true&key='
url = serviceurl+app_key


js_barrios = barrios.get_barrios_data(nombres_barrios)
js_ruta = ruta.get_ruta_data(url, js_barrios,10)

print (json.dumps(js_ruta, indent=4))







# print(durations)


# print(json.dumps(js['routes'][0]['legs'][0]['distance'], indent=4))
