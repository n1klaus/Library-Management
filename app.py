#!/usr/bin/python3

"""Main Flask App"""

from flask import Flask, render_template
from flask_cors import CORS
from models.base_model import sa
from api.v1.views import app_views
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

session_options = {
    'autocommit': False,
    'autoflush': False,
    'expire_on_commit': False  # Disable autorefresh of attributes after commit
}

with app.app_context():
    sa.init_app(app=app)
    sa.session = scoped_session(
        sessionmaker(
            bind=sa.engine,
            **session_options))
    sa.drop_all()
    sa.create_all()


@app.teardown_appcontext
def delete_session(exception=None):
    """
    Ensures that the session is properly closed and removed at the end
    of each request or application context.
    """
    sa.session.remove()


@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def home():
    """Renders home page"""
    return render_template('home.html')


@app.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Renders status page"""
    return render_template('status.html')


@app.route('/help', methods=['GET'], strict_slashes=False)
def help():
    """Renders help page"""
    return render_template('help.html')


@app.route('/settings', methods=['GET'], strict_slashes=False)
def settings():
    """Renders settings page"""
    return render_template('settings.html')


if __name__ == '__main__':
    with app.app_context():
        app.register_blueprint(app_views)

    app.run(debug=True, load_dotenv=True)
