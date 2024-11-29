from flask import Flask
from config.config import Config
from routes.students_routes import register_student_routes
from utils.db import db

app = Flask(__name__)

app.config.from_object(Config)

db.init_app(app)

register_student_routes(app)

with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
