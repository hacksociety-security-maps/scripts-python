import urllib
import urllib2
import json

def get_data(url):

    # print('Retrieving', url)
    req = urllib2.Request(url)
    uh = urllib2.urlopen(req)
    data = uh.read()
    # print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
        return js
    except:
        js = None

    if not js:
        print('==== Failure To Retrieve ====')
        print(data)
        return None

