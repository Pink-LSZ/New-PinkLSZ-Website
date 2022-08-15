from flask import render_template, jsonify
from app import app

@app.route('/')
def index():
    return jsonify(app.config['ENVIRONMENT'])