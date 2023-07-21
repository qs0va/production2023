from geopy import Nominatim

g = Nominatim(user_agent="coder")

def incode(street, number):
    loc = g.geocode("Санкт-Петербург, " + street + ", " + str(number))
    try:
        ans = [loc.latitude, loc.longitude, loc.address]
    except AttributeError:
        raise Exception('Cannot find given address')
    
    return ans
