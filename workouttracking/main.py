
import os
import requests
from datetime import datetime
WEIGHT_KG = 60
HEIGHT_CM = 160
AGE = 19
GENDER = "female"
#APP_ID = "app_f95da5b2b2234ea6ad75b468"
APP_ID = os.environ["APP_ID"]

API_KEY = os.environ["APP_KEY"]

USER = os.environ["USERNAME"]
PASS = os.environ["PASSWORD"]
url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}
exercise_info = input("What did you do today?")
parameters = {
    "query" : exercise_info,
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER
}
response = requests.post(url = url, headers = headers, json = parameters)
result = response.json()
day = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")
sheety_endpoint = os.environ["SHEET_ENDPOINT"]
for exercise in result["exercises"]:
    inputs = {
        "workout" : {
            "date" : day,
            "time" : current_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"]
        }
    }
    response1 = requests.post(url = sheety_endpoint, json = inputs, auth = (USER, PASS))
    print(response1)


