import os
import requests
from datetime import datetime

APP_ID = os.environ["NUTRITIONIX_APP_ID"]
API_KEY = os.environ["NUTRITIONIX_APP_KEY"]

header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
exercise_params = {
    "query": input("Tell me which exercises you did: "),
    "gender": input("What is your gender? (male/female) ").lower(),
    "weight_kg": float(input("What is your weight? (KG) ")),
    "height_cm": int(input("What is your height? (CM) ")),
    "age": int(input("What is your age? "))
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise/"

response = requests.post(url=exercise_endpoint, headers=header, json=exercise_params)
exerc_data = response.json()

now = datetime.now()
today = now.strftime("%d/%m/%Y")
current_time = now.strftime("%H:%M:%S")

exercise = exerc_data['exercises'][0]['name'].title()
duration = exerc_data['exercises'][0]['duration_min']
calories = exerc_data['exercises'][0]['nf_calories']

headers = {
    "Authorization": os.environ["SHEETY_EXERCISES_AUTH"]
}

sheety_endpoint = os.environ["SHEETY_SHEET_ENDPOINT"]

actual_params = {
    "página1": {
        "date": today,
        "time": current_time,
        "exercise": exercise,
        "duration": duration,
        "calories": calories
    }
}
sheety_response = requests.post(url=sheety_endpoint, headers=headers, json=actual_params)