import urllib
import json

def get_data(url):

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        return js
    except:
        js = None

    if not js:
        print('==== Failure To Retrieve ====')
        print(data)

