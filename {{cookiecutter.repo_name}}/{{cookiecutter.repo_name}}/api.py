# -*- coding: utf-8 -*-
import logging

from flask import Blueprint, jsonify, request
from flask.ext.restful import Api, Resource

logger = logging.getLogger(__name__)
api_bp = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(api_bp)
