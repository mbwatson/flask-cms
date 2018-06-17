from flask import Flask
app = Flask(__name__)

import flaskcms.routes
from flaskcms.models import Page


