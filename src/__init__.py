import os
import src.config as config
from dotenv import load_dotenv

from flask import Flask

from src import error_handlers

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# app.config["sample_img"] = os.path.join(config.path, "test_images", "pelican.jpg")
app.register_blueprint(error_handlers.blueprint)

from src.routes import routes
