import simplejson
import urllib.request

def getAPIKey():
    file = open("google_map_api_key.txt", "r")
    API_KEY = file.readline()
    file.close()
    return API_KEY[:-1]  # remove the new line character

def getPlaceID(API_KEY, address):
    address = address.replace(" ", "%20")
    url = "https://maps.googleapis.com/maps/api/geocode/json?key={0}"\
        "&new_forward_geocoder=true&address={1}".format(API_KEY, address)
    result = simplejson.load(urllib.request.urlopen(url))
    return result['results'][0]['place_id']

def getDrivingTime(API_KEY, orig_place_ID, dest_place_ID):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"\
        "?origins=place_id:{0}&destinations=place_id:{1}&mode=driving"\
        "&language=en-EN&sensor=false"\
        "&key={2}".format(orig_place_ID, dest_place_ID, API_KEY)
    result = simplejson.load(urllib.request.urlopen(url))
    print(result['rows'][0]['elements'][0]['duration']['text'])

API_KEY = getAPIKey()

address = "280 Easy St"
place_ID = getPlaceID(API_KEY, address)

FB_address = "1 Hacker Way"
FB_place_id = getPlaceID(API_KEY, FB_address)

getDrivingTime(API_KEY, place_ID, FB_place_id)
