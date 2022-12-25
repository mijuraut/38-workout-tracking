import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 183
AGE = 40

APP_ID = "31111960"
API_KEY = "a080bc2fc55f5f7f74023e418f45609c"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/d9ce15d90b4cced2cc70a4a14babbee8/100DaysOfCode:MyWorkouts/workouts"

exercise_text = input("Which exercises you did? (eg.\"I walked 100 m\")")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()

# Step 4 start

today_date = datetime.now().strftime("%d.%m.%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

    print(sheet_response.text)
