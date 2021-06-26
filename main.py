import requests
from requests import api
import datetime as dt

app_id = ''
app_key = ''
sheety_token = '%'

workout_endpoint = 'https://trackapi.nutritionix.com/v2/natural/exercise'
sheety_endpoint = 'https://api.sheety.co/31a86792fd95429388193024970a7b21/workoutTracking/workouts'

headers = {
    'x-app-id': app_id,
    'x-app-key': app_key,
}

sheety_headers = {
    'Authorization': 'Bearer NbTqCor7W5FESGB%'
}

exercise = input('Enter exercise: ')

exercise = {
    "query": exercise,
    "gender": "male",
    "weight_kg": 63,
    "height_cm": 160,
    "age": 22
}

response = requests.post(url=workout_endpoint, json=exercise, headers=headers)
result = response.json()

date_time = dt.datetime.now()
date = date_time.strftime('%d %B %Y')
time = date_time.strftime('%H:%M')

for exercise in result['exercises']: 
    workout = {
        'workout': {
            'date': date,
            'time': time,
            "exercise": exercise["name"].title(),
            "duration": str(exercise["duration_min"]),
            "calories": exercise["nf_calories"]
        }
    } 

response = requests.post(url=sheety_endpoint, json=workout, headers=sheety_headers)
