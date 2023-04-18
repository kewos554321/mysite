# flask_project/__init__.py

from flask import Flask
# from ..config import config_by_name, key

app = Flask(__name__)
# app.config.from_object(config_by_name[key])

from .views import views
