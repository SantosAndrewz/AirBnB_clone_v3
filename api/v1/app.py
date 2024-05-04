#!/usr/bin/python3
"""
Creates a flask app that is used to start an api
"""


from flask import Flask
from models import storage
from app.v1.views import api_views
import os

app = Flask(__name__)

"""Registering the app_views blueprint"""
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """closes the storage"""
    storage.close()

if __name__ == "__main__":
    api_host = os.gentenv('HBNB_API_HOST', '0.0.0.0')
    api_port = int(os.gentenv('HBNB_API_PORT', '5000'))
    app.run(host=app_host, port=app, threaded=True)
