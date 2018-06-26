# weather_station.py 6/26/18

import requests

# OpenWeatherMap API: https://openweathermap.org/api
def get_api_data(zipcode):
    package = {
        'APPID': 'b07b5a2318c94aaba3baad83883d16dd',
        'zip': '{}'.format(zipcode)
    }

    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=package)
    response = r.json()
    #print(r.url)
    # print("Status code: {}".format(r.status_code))
    return response

def k_to_c(kelvin_temp):
    celsius_temp = kelvin_temp - 273.15
    return celsius_temp

def k_to_f(kelvin_temp):
    fahrenheit_temp = ((kelvin_temp - 273.15) * 9 / 5) + 32
    return fahrenheit_temp

def main():
    zip_code = input("Please enter the zipcode of the city: ")
    api_data_dict = get_api_data(zip_code)

    kelvin_temp = int(api_data_dict['main']['temp'])
    kelvin_temp_min = int(api_data_dict['main']['temp_min'])
    kelvin_temp_max = int(api_data_dict['main']['temp_max'])

    while True:
        temp_unit = input("Would you like the temperature displayed in (C)elsius or (F)ahrenheit?: ")

        if temp_unit.lower() in ['c', 'celsius']:
            print("Displaying today's temperature in Celsius.")
            print("Current Temperature: {}".format(k_to_c(kelvin_temp)))
            print("Minimum Temperature: {}".format(k_to_c(kelvin_temp_min)))
            print("Maximum Temperature: {}".format(k_to_c(kelvin_temp_max)))
            break
        elif temp_unit.lower() in ['f', 'fahrenheit']:
            print("Displaying today's temperature in Fahrenheit.")
            print("Current Temperature: {}".format(k_to_f(kelvin_temp)))
            print("Minimum Temperature: {}".format(k_to_f(kelvin_temp_min)))
            print("Maximum Temperature: {}".format(k_to_f(kelvin_temp_max)))
            break
        else:
            print("Not a vaild input. Try again.")

main()
