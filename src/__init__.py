import os

from torchvision.models import mobilenet
import src.config as config
from dotenv import load_dotenv
from src.models import MobileNet
from flask import Flask

from src import error_handlers

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
model = MobileNet()
# app.config["sample_img"] = "E://TSAI/EMLO/EMLO-session3/test_images/triceratops.jpg"
app.register_blueprint(error_handlers.blueprint)

from src.routes import routes
