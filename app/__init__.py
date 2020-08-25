from flask import Flask

app = Flask(__name__)

from app import public_routes
from app import admin_routes
