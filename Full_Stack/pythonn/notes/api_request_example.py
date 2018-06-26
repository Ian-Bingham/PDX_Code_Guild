# # api_request_example.py 6/26/18
#
# import requests
#
# # chuck norris jokes
# r = requests.get('http://api.icndb.com/jokes/random')
# # print(r.status_code)
# # print(r.text)
# response = r.json()
# # print(response['type'])
# print(response['value']['id'])
# print(response['value']['joke'])
# print(response['value']['categories'])
#
#
# # openweathermap
import requests

package = {
    'APPID': 'c6311d9ec7ce3538db5dfefb668ed619',
    'q': 'Portland',
    'units': 'imperial'
}

r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=package)

response = r.json()
print(r.status_code)
print(response['main']['temp'])
print(r.url)
