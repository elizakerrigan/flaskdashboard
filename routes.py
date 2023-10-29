from flask import Blueprint, render_template
from db.db_modules import get_db
from models import Weather

main = Blueprint('main', __name__)

@main.route('/')
def index():
    weather_data = Weather.query.limit(10).all()  # fetches all records
    return render_template('index.html', weather_data=weather_data)
