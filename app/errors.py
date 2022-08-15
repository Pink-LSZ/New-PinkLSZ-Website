from flask import render_template, redirect, url_for, session, flash
from app import app
from functools import wraps

from flask import render_template

@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404