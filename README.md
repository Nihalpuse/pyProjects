
Weather App
Welcome to the Weather App! This application provides the current weather conditions for any city using the WeatherAPI.

Features
Greets the user based on the current time.
Prompts the user to enter the name of a city.
Fetches and displays the current temperature and weather condition for the specified city.
Requirements
Python 3.x
requests library
json library
datetime library
pyttsx3 library (for text-to-speech functionality, though it’s not used in the provided code)
Installation
Clone the repository to your local machine.
bash
Copy code
git clone https://github.com/yourusername/weather-app.git
Navigate to the project directory.
bash
Copy code
cd weather-app
Install the required Python libraries.
bash
Copy code
pip install requests pyttsx3
Usage
Run the weather_app.py script.
bash
Copy code
python weather_app.py
Enter the name of the city when prompted.
The app will display the current temperature and weather condition for the specified city.
Example
plaintext
Copy code
********************Welcome to Weather App***********************
Good afternoon!

Enter the Name of the city : London

Weather details for London are as follows:
Temperature is 20 Degrees
Current condition is : Partly cloudy
API
This app uses the WeatherAPI to fetch weather data. You need to have an API key from WeatherAPI to use this app. Replace the placeholder API key (e6f8a6ba9cde40339b382657241107) with your own API key in the url variable.

Contributing
If you want to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature-branch).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature-branch).
Create a new Pull Request.
