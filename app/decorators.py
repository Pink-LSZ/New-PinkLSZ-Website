from flask import render_template, redirect, url_for, session, flash
from app import app
from functools import wraps

def login_required(f):
	"""
	Sets @login_required decorator to require
	login on authenticated pages
	"""
	@wraps(f)
	def wrap(*args, **kwargs):
		# if user is not logged in, redirect to login page      
		if not session:
			return redirect(url_for('login'))
		return f(*args, **kwargs)
	return wrap