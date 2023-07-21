import requests
import json

def incode(street, number):
    q = "Санкт-Петербург, " + street + ", " + str(number)
    resp = requests.get('http://51.250.101.212/search?q=' + q + '&format=json&limit=1')

    j = json.loads(resp.content)
    try:
        loc = j[0]
    except IndexError:
        raise Exception('Cannot find given address')

    return [loc['lat'], loc['lon'], loc['display_name']]
