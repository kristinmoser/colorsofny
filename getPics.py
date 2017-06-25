import requests

def getVenues(cityName):
    venuesJSON = getVenuesJSON(cityName)

    venues = []
    for x in xrange(2):

        aVenue = venuesJSON[x]['venue']
        venueName = aVenue['name']
        venuePhotoData = aVenue['featuredPhotos']['items'][0]
        venuePrefix = venuePhotoData['prefix']
        venueSize = str(venuePhotoData['width']) + "x" + str(venuePhotoData['height'])
        venueSuffix = venuePhotoData['suffix']

        venueURL = venuePrefix + venueSize + venueSuffix

        venueInfo = [venueName,venueURL]

        venues.append(venueInfo)

    return venues


def getVenuesJSON(cityName):
    url = "https://api.foursquare.com/v2/venues/explore?v=20161016&near="
    intentAndKeys= "&intent=checkin&client_id=HA2GOHRQRIK2QK001COZCU2GD4ZDT4NTBKIBCS0144AHEMUS&client_secret=JT4CIEBPNLEFMPH3ZEUCTESCO0OI2S15AAHHMXJVP4QW5M2W&venuePhotos=1"

    url = url + cityName + intentAndKeys

    r = requests.get(url)

    return r.json()['response']['groups'][0]["items"]

#if __name__ == "__main__":
 #   venues = getVenues("New York")
   # print ("Hello world")