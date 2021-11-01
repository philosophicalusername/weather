# Initial Weather Attempt

import json
import requests

print('Welcome to Whether the Weather will Wither')
print("")
print('How would you like to lookup your data?')

city_name = ""
zipcode = ""

whichone = input("City or Zip?")

if whichone == "City" or "city":
    city_name = input("Please enter your city name:  ")
else:
    zipcode = input("Please enter your zip code:  ")
    
#while whichone == 'City' and whichone != 'Zip':
#    print("Please enter your city name:")
#    city_name = input()
#    return

api_key = "5c492a5a90926c996374f7965ba323c6"

lat = "36.3729"
lon = "94.2088"
beginningurl = "http://api.openweathermap.org/data/2.5/weather?"
url = beginningurl + "appid=" + api_key +"&q=" + city_name
infodump = requests.get(url)
allData = json.loads(infodump.text)

if allData["cod"] != "404":
    main = allData["main"]
    current_temp = main["temp"]
    current_pressure = main["pressure"]
    current_humidity = main["humidity"]
    endInfo = allData["weather"]
    weather = endInfo[0]["description"]
    print(" Temperature = " + str(current_temp) +
          "\n Pressure = " + str(current_pressure) +
          "\n Humidity = " + str(current_humidity) +
          "\n Description = " + str(weather))
else:
    print(" City not Found ")

print(endInfo)
