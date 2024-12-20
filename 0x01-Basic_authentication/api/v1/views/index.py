#!/usr/bin/env python3
"""Index view module for the API."""

from flask import jsonify, abort
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', methods=['GET'], strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {
        'users': User.count()
    }
    return jsonify(stats)


@app_views.route('/unauthorized', methods=['GET'], strict_slashes=False)
def unauthorized_route():
    """GET /api/v1/unauthorized
    Returns:
      - Raises a 401 error
    """
    abort(401)


@app_views.route('/forbidden', methods=['GET'], strict_slashes=False)
def forbidden_route():
    """GET /api/v1/forbidden
    Returns:
      - Raises a 403 error
    """
    abort(403)
