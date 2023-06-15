#!/usr/bin/python3

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from api.v1.views import app_views

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'


app.register_blueprint(app_views)
sa = SQLAlchemy(app)

if __name__ == '__main__':
    with app.app_context():
        sa.create_all()
    app.run(debug=True, load_dotenv=True)
