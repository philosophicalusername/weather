# Beginning - loading json, time, and requests

import json
import requests
import time

# Initial welcome message
print('\nWelcome to Whether the Weather will Wither')
print("")

# Global variable for api key and setting input to None
API_KEY = "5c492a5a90926c996374f7965ba323c6"

user_input = None

# helper function to make re-running or ending program work
def helper():
    """Helper function to re-run program"""
    while keep_running():
        keep_running()

# Function to query user if they would like to look for another location
def keep_running():
    """Function to ask user if they wish to continue or not"""
    answer = input("\nWould you like to check another location?" + "\nYes or No: ")
    if answer == "yes":
        print("\nGreat! Let's continue...")
        time.sleep(.25)
        print("\n  ヘ(^_^ヘ)    °\(^▿^)/°")
        print("")
        ask_user()
    elif answer == "Yes":
        print("\nGreat! Let's continue...")
        time.sleep(.25)
        print("\n  ヘ(^_^ヘ)    °\(^▿^)/°")
        print("")
        ask_user()
    else:
        print("\nThank you for your usage.")
        time.sleep(1)
        print("\n         Goodbye")
        return False

# Funtion to ask user for information as well as running web query from API
def ask_user():
    """Main function that asks for user input and performs query of API"""
    user_input = input("Please enter the city name or zipcode for the weather: ")
    def user_responded():
        city_name = user_input
        upper_name = city_name
        city_name_response = city_name
        url1 = "http://api.openweathermap.org/data/2.5/weather?"
        url2 = url1 + "appid=" + API_KEY + "&q=" + city_name_response + "&units=imperial"
        try:
            infodump_city = requests.get(url2)
            print("\n    Connection available")
            time.sleep(.5)
            print("\n        Retrieving Data")
            time.sleep(.5)
            all_data_city = json.loads(infodump_city.text)
        except:
            print("Something went wrong...")
        if all_data_city["cod"] != "404":
            main = all_data_city["main"]
            current_temp_city = main["temp"]
            current_pressure_city = main["pressure"]
            current_humidity_city = main["humidity"]
            end_city = all_data_city["weather"]
            weather = end_city[0]["description"]
            print("\n  The weather in " + upper_name.title() + " is as follows:")
            print("\n        Temperature = " + str(current_temp_city) + "° Farenheit" + "\n " +
                "\n        Pressure = " + str(current_pressure_city) + " millibars" + "\n " +
                "\n        Humidity = " + str(current_humidity_city) + "%" + "\n " +
                "\n        Description = " + str(weather.title()))
            helper()
        else:
            print("\n    City not found")
            helper()
    user_responded()

# Calling the main function
ask_user()

# Part of the helper function at beginning of program
if __name__ == "__helper__":
    helper()
