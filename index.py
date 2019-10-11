from flask import Flask, request, url_for
from flask import redirect, render_template, session

app = Flask(__name__)

@app.route('./index')
def index():
    return render_template('index.html')