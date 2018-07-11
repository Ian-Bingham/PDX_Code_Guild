# random_users.py 7/11/18

import requests

# get 5 random people's information from this api
# and pretty print some information
def get_n_peoples_info(n):
    for i in range(n):
        r = requests.get('https://api.randomuser.me/?results=5')
        response = r.json()
        # print(r.url)
        # print(r.status_code)
        # print(response['results'][0]['name'])
        titlename = response['results'][0]['name']['title'].capitalize()
        firstname = response['results'][0]['name']['first'].capitalize()
        lastname = response['results'][0]['name']['last'].capitalize()

        email = response['results'][0]['email']
        username = response['results'][0]['login']['username']
        registration_date = response['results'][0]['registered']['date'][:10]
        reg_month = registration_date[5:7]
        reg_day = registration_date[-2:]
        reg_year = registration_date[:4]
        birth_date = response['results'][1]['dob']['date'][:10]
        birth_month = birth_date[5:7]
        birth_day = birth_date[-2:]
        birth_year = birth_date[:4]

        print('*' * 80)
        print(f"Name: {titlename} {firstname} {lastname}")
        print(f"Email: {email}")
        print(f"Username: {username}")
        print(f"Registration Date: {reg_month}/{reg_day}/{reg_year}")
        print(f"Birth Date: {birth_month}/{birth_day}/{birth_year}")

get_n_peoples_info(5)
