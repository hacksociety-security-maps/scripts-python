import data
import re
import json
import math


def get_ruta_data(url, js_barrios, tresh):

    durations = list()
    js = data.get_data(url)
    calculo = dict()

    calculo = {'rutas': []}
    print (calculo)

    conteo = int()

    for route in js['routes']:
        print('\n' + route['summary'])
        for leg in route['legs']:
            durations.append(re.findall('\d+', leg['duration']['text'])[0])
            for step in leg['steps']:
                # print ('origin is' + json.dumps(step['start_location']) + 'end is= ' + json.dumps(step['end_location']))
                lat2 = step['end_location']['lat']
                lon2 = step['end_location']['lng']

                for barrio in js_barrios['barrios']:
                    lat1 = barrio['latitud']
                    lon1 = barrio['longitud']
                    print ('=======' + barrio['nombre'])

                    dist = math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(
                        lon1 - lon2)) * 6371
                    print (dist)
                    if dist > tresh:
                        conteo = conteo + 1

        calculo['rutas'].append({'nombre':route['summary'], 'conteo': conteo})
        conteo = 0

    print (json.dumps(calculo, indent=4))
    # print(json.dumps(js_barrios, indent=4))
    cont_min = 9999
    for ruta in calculo['rutas']:
        if ruta['conteo'] < cont_min:
            cont_min = ruta['conteo']
            nombre = ruta['nombre']

    for route in js['routes']:
        if nombre in route['summary']:
            return route


