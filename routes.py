from flask import Blueprint, render_template
import datetime
import requests
import os
from dotenv import load_dotenv
import db 
from db.db_modules import get_db
from models import Weather
from sqlalchemy import func

main = Blueprint('main', __name__)

load_dotenv()
API_KEY = os.getenv("API_KEY")

Part = "current,minutely,daily,alerts"
Lat  = f"27.4679"
Lon  = f"153.0281"

@main.route('/')
def index():
    latest_entry =  Weather.query.order_by(Weather.date_time.desc()).first()
    now = datetime.datetime.now()

    if not latest_entry: 
        raise Exception("Database Error: No Entries found in [weather] table. Please check Data connections")
    
    if not latest_entry or (now - latest_entry.date_time).seconds >= 3600: 
        response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={Lat}&lon={Lon}&units=metric&exclude={Part}&appid={API_KEY}")
        if response.status_code == 200: 
            weather_data = response.json()['hourly']
            for data in weather_data:
                dt_object = datetime.datetime.fromtimestamp(data['dt'])
                if dt_object > latest_entry.date_time: 
                    temperature = data['temp']
                    new_entry = Weather(
                        date_time = dt_object
                        , date = dt_object.date()
                        , time = dt_object.time()
                        , temp_min = None
                        , temp_max = temperature
                        , humidity = data['humidity']
                        , wind_speed = data['wind_speed']
                        , weather_description = data.weather['description']
                        , city = 'Brisbane'
                    )
                    db.session.add(new_entry)
            db.session.commit()
            print(weather_data)
    weather_data = Weather.query.limit(10).all()  # fetches 10 records
    return render_template('index.html', weather_data=weather_data)
