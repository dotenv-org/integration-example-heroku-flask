# app/main.py
import os
from dotenv_vault import load_dotenv
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
  hello = os.getenv("HELLO")
  return f"<p>Hello, {hello}!</p>"
