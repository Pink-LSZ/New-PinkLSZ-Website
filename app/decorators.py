from flask import render_template, redirect, url_for, session
from app import app
from functools import wraps

def test_one(f):
	"""
	Sets @login_required decorator to require
	login on authenticated pages
	"""
	@wraps(f)
	def wrap(*args, **kwargs):
		# if user is not logged in, redirect to login page      
		if not session:
			return redirect('http://google.com')
		return f(*args, **kwargs)
	return wrap