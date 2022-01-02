from flask import Flask, render_template
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config.from_object("config.Config")
api = Api(app)
db.init_app(app)


with app.app_context():
    from routes.api import *
    from routes.main import *
    from models import Plant, Employee

    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
