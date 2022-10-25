# app/main.py
import os
from dotenv_vault import load_dotenv

hello = os.getenv('HELLO')

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  return f"<p>Hello, {hello}!</p>"
