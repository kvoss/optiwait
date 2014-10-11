import urllib
import urllib2

import json
import pprint

# RET_MOCK = {
#    "destination_addresses" : [ "Regina, SK, Canada" ],
#    "origin_addresses" : [ "Saskatoon, SK, Canada" ],
#    "rows" : [
#       {
#          "elements" : [
#             {
#                "distance" : {
#                   "text" : "258 km",
#                   "value" : 257833
#                },
#                "duration" : {
#                   "text" : "2 hours 46 mins",
#                   "value" : 9980
#                },
#                "status" : "OK"
#             }
#          ]
#       }
#    ],
#    "status" : "OK"
# }


API_KEY = 'AIzaSyD-YI1P-lBIjUhmkhcAvOKKc60q1L1K2wE'
URL = 'https://maps.googleapis.com/maps/api/distancematrix/json'

def get_raw_distances(loc, clinics):

    params = urllib.urlencode({ 
        'origins' : loc,
        'destinations': '|'.join(clinics),
        'key' : API_KEY,
        })

    #print params
    response = urllib2.urlopen('?'.join([URL, params])).read()
    ret = json.loads(response)
    distances = zip(clinics, ret['rows'][0]['elements'])
    return distances

def get_distances(loc, clinics):
    """ returns a list of tuples with clinic address and distance to it

    loc -- location -- string
    clinics -- list of strings representing addressed of clinics
    """
    raw = get_raw_distances(loc, clinics)
    #print raw
    #ret = map(lambda c, e: (c, e['distance']['value'] / 1000), raw)
    ret = map(lambda (c, e): (c, e['distance']['text']), raw)
    return ret

#print get_distances('Saskatoon', ['Regina, SK', '110 Science Place, Saskatoon'])

