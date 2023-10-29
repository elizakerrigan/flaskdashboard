from flask import Flask, render_template
from routes import main
import config
from db.db_modules import db


app = Flask(__name__)
app.register_blueprint(main)
app.config.from_object(config)
db.init_app(app)

if __name__ == '__main__':
    app.run()