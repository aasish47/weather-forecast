import requests
from geopy.geocoders import ArcGIS

# user input 
city = input("Enter a city name: ")
# my api 
API_KEY="07941f17bd68324fa7a99f76de9f5890"
# it's the base url we are going to use in out fetching
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# function to get the latitude and longitude of a city
def get_lat_lon(city):
    geolocator = ArcGIS()
    location = geolocator.geocode(city)
    if location is not None:
        latitude = location.latitude
        longitude = location.longitude
        return latitude, longitude
    else:
        return None, None
latitude, longitude = get_lat_lon(city)

# building our request url
request_url = f"{BASE_URL}?lat={latitude}&lon={longitude}&appid={API_KEY}"
# storing the response
response = requests.get(request_url)
# checking the response if 200 then success else error
if response.status_code==200:
    # storing the fetched data in the variable data
    data = response.json()
    """
        {'coord': {'lon': -74.0071, 
        'lat': 40.7145}, 
        'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 
        'base': 'stations', 
        'main': {'temp': 300.64, 'feels_like': 300.98, 'temp_min': 298.68, 'temp_max': 302.18, 'pressure': 1010, 'humidity': 49}, 
        'visibility': 10000, 
        'wind': {'speed': 4.63, 'deg': 320}, 
        'clouds': {'all': 0}, 'dt': 1690044653, 
        'sys': {'type': 2, 'id': 2008101, 'country': 'US', 'sunrise': 1690018987, 'sunset': 1690071688}, 'timezone': -14400, 
        'id': 5128581, 
        'name': 'New York',
        'cod': 200}
        as you can see above it's the json file we fetched and stored in the data variable for city='new york'
        here we are getting into the data to get the specific details that we want
    """
    print("For",city,":")
    weather = data['weather'][0]['description']
    print("weather: ",weather)
    temperature = round(data["main"]["temp"]-273.15,2)
    print("temperature:",temperature,"Celsius")
else:
    print("an Error occured.")