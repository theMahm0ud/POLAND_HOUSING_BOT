import googlemaps

API_KEY = 'AIzaSyCBD4eIzezZ-ggnXw5jPWGsXdGVVJIqrAM'

def get_lat_lng(address):
    """
    Get the latitude and longitude of an address using Google Maps Geocoding API
    """
    gmaps = googlemaps.Client(key=API_KEY)
    geocode_result = gmaps.geocode(address)
    if len(geocode_result) > 0:
        location = geocode_result[0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None


def generate_map_popup(address, api_key):
    gmaps = googlemaps.Client(key=api_key)
    geocode_result = gmaps.geocode(address)

    if len(geocode_result) == 0:
        return None

    location = geocode_result[0]['geometry']['location']
    map_url = f"https://www.google.com/maps/search/?api=1&query={location['lat']},{location['lng']}"

    return map_url