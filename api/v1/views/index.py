#!/usr/bin/python3
"""
A module defining the routes for API.v1
"""

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """ returns api status"""
    return jsonify({"status"="OK"})


@app_views.route("/stats")
def get_stats():
    """Retrieves the number of each object by type using the count() method"""
    return jsonify({
        "amenities": storage.count("Amenity"),
        "users": storage.count("User"),
        "states": storage.count("State"),
        "cities": storage.count("City"),
        "places": storage.count("Place"),
        "reviews": storage.count("Review"),
    })
