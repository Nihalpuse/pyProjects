import requests
import json
from datetime import datetime
import pyttsx3
def greet_user():
    current_time = datetime.now()
    current_hour = current_time.hour

    if current_hour < 12:
        greeting = "Good morning!"
    elif 12 <= current_hour < 18:
        greeting = "Good afternoon!"
    else:
        greeting = "Good evening!"

    print(greeting)


# Welcoming user
print("\n********************Welcome to Weather App***********************")
greet_user()


# Taking Input from User for their City
city = input("\nEnter the Name of the city : ")

# Providing city value in the api to search for respective city's Data
url = f"http://api.weatherapi.com/v1/current.json?key=e6f8a6ba9cde40339b382657241107&q={city}&aqi=no"

#Pulling Requests from URL
r = requests.get(url)

# Converting String to Dictionary so that we can extract details 
weatherdict = json.loads(r.text) 
temp = weatherdict["current"]["temp_c"]
wcondition =weatherdict["current"]["condition"]["text"]

# Displaying Output to User
print(f"\nWeather details for {city} are as follow :-")
print(f"Temperature is {temp} Degrees")
print(f"Current condition is : {wcondition}\n\n")