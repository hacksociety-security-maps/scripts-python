# Copyright 2015 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START app]
import logging

import json

from flask import Flask

import barrios
import ruta


app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    app_key = 'AIzaSyBv0RCGswuYS5g52SBUpMvZKCElkfzPdtA'

    nombres_barrios = ['teusaquillo', 'la florida occidental', 'samper mendoza', 'estacion central', 'paloquemao','quinta paredes']
    serviceurl = 'https://maps.googleapis.com/maps/api/directions/json?origin=Universidad+nacional+de+colombia,Bogota&destination=Centro+comercial+calima,Bogota&alternatives=true&key='
    url = serviceurl+app_key


    js_barrios = barrios.get_barrios_data(nombres_barrios)
    js_ruta = ruta.get_ruta_data(url, js_barrios,10)

    print (json.dumps(js_ruta, indent=4))

    return json.dumps(js_ruta, indent=4)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END app]







