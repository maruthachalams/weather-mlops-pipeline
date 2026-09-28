from fastapi import FastAPI
from weather_scraper import MyScraper
import joblib

app = FastAPI()

model = joblib.load("temperature_model.pkl")

@app.get("/")
def read_home():
    return {"message": "My Weather API is alive!"}

@app.get("/weather")
def get_weather():
    bot = MyScraper()
    weather_data = bot.fetch_data()
    return weather_data

@app.get("/predict/{day}")
def predict_temperature(day: int):
    predicted_temp = model.predict([[day]])
    return{
        "city" : "coimbatore",
        "day_input" : day,
        "predicted_temp_c" : round(predicted_temp[0], 2)
    }


