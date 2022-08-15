from flask import render_template, jsonify
from app import app
from app.decorators import test_one

@app.route('/')
def index():
    return jsonify(app.config['DEBUG'])