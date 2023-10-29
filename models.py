from db.db_modules import db

class Weather(db.Model):
    __tablename__ = 'weather'
    date = db.Column(db.Date, primary_key = True)
    time = db.Column(db.Time, primary_key = True)
    temp_min = db.Column(db.Float)
    temp_max = db.Column(db.Float)
    humidity = db.Column(db.Float)
    wind_speed = db.Column(db.Float)
    weather_description = db.Column(db.String(50))
    city = db.Column(db.String(50))