from flask import render_template, redirect, url_for, session, flash, abort
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

def admin_required(f):
	"""
	Sets @admin_required decorator to require
	admin on authenticated pages
	"""
	@wraps(f)
	def wrap(*args, **kwargs):
		account = app.db.GetAccount(session['username'])
		if not account['isadmin'] == 'True':
			return abort(404)
		return f(*args, **kwargs)
	return wrap

def dev_required(f):
	"""
	Sets @admin_required decorator to require
	admin on authenticated pages
	"""
	@wraps(f)
	def wrap(*args, **kwargs):
		account = app.db.GetAccount(session['username'])
		if not account['isdev'] == 'True':
			return abort(404)
		return f(*args, **kwargs)
	return wrap