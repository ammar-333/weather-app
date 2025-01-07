## Weather Application

Project Overview

Weather Application is a desktop application that was designed using Python and based on the Tkinter library. It is able to display real-time weather in any city in the world with the help of the WeatherAPI service. It will display the following data: temperature, conditions, humidity, wind speed, and pressure of the atmosphere. It also includes an icon to give a representation of the current condition.

----------------------------------------------------------------
Features

1. User-Friendly Interface: A clean, modern GUI with intuitive design elements.
2. Real-Time Weather Data: Fetches and displays the most recent weather of any entered city.
3. Weather Details:
   - City and Country
   - Temperature in Celsius
   - Weather condition description
   - Humidity in percentage
   - Wind speed in kph
   - Atmospheric pressure in mb
4. Dynamic Weather Icon: It shows the icon according to the weather of a particular area.
5. Interactive Input field: An input field that fills up and changes its color after hover on to improve customer satisfaction.

---------------------------------------------------------------
Requirements

Below is what you require running this application:

1. Python 3.x
2. Dependency on Python Package List:
	* `tkinter` - Normally preinstalled along with the installation of python.
	* `requests`
	* `Pillow`

---------------------------------------------------------------
Installation
Setting it up

Dependencies

After the above setting run this following command and let all libraries install first

pip install requests pillow

---------------------------------------------------------------

Usage Instructions

1. Run the Application: Execute the script to launch the application.
2. City Name Input: Type the city name in the text area.
3. Search Button Click: The `Search` button fetches and displays the weather information.
4. Weather Information Display: The Weather information and icon will be displayed below the text area.

----------------------------------------------------------

Project Structure

The codebase is organized with the following directory structure:

- Main Class: `WeatherApp`
- Controls the GUI layout and user interactions.
  - Integrates API calls and displays results.
- Functions:
  - `setup_ui()`: Sets up the GUI components and their styles.
  - `get_weather()`: Fetches weather data from the WeatherAPI.
  - `display_weather(data)`: Displays the weather information and icon in the GUI.

