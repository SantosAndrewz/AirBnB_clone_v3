#!/usr/bin/python3
"""
Creates a Flask app instance, registers app_views and closes storage.
"""

from flask import Flask
from models import storage
from api.v1.views import app_views
from flask_cors import CORS
import os


app = Flask(__name__)


CORS(app, resourses=r"/*", origins="0.0.0.0")
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(exception):
    """close storage"""
    storage.close()


@app.errorhandler(404)
def error_Not_found(error):
    """handles the error 404 then responds with a JSON-formatted response"""
    return (jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    if os.getenv('HBNB_API_HOST') is None:
        HBNB_API_HOST = '0.0.0.0'
    else:
        HBNB_API_HOST = os.getenv('HBNB_API_HOST')
    if os.getenv('HBNB_API_PORT') is None:
        HBNB_API_PORT = 5000
    else:
        HBNB_API_PORT = int(os.getenv('HBNB_API_PORT'))
    app.run(host=HBNB_API_HOST, port=HBNB_API_PORT, threaded=True)
