from flask import render_template, jsonify, request, redirect, session, flash, url_for, send_from_directory
from app import app
from app.decorators import login_required, admin_required, dev_required
from app.errors import page_not_found
from app.hfapi import Get_Access_Token
from app.discord import get_discord_access_token, get_discord_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hf/images/<filename>')
def servefile(filename):
    return send_from_directory('../hf/images', filename)

@app.route('/login')
@app.route('/profile')
@app.route('/profile/verifydiscord')
def login():
    if 'code' in request.args:
        access_token = get_discord_access_token(app.config['DISCORDCLIENT'], app.config['DISCORDSECRET'], app.config['DISCORDREDIRECTURI'], request.args['code'])
        discorduser = get_discord_user(access_token)
        username = f"{discorduser['username']}#{discorduser['discriminator']}"
        email =  discorduser['email']
        discriminator =  discorduser['discriminator']
        name =  discorduser['username']
        avatar =  discorduser['avatar']
        userid =  discorduser['id']
        if app.db.checkexists(username):
            flash('Successfully Logged In')
            session['loggedin'] = True
            session['username'] = username
        else:
            app.db.query(f'INSERT INTO users (username, email, discordId, discriminator, avatar) VALUES ("{username}", "{email}", "{userid}", "{discriminator}", "{avatar}")', querytype="insert")
            session['loggedin'] = True
            session['username'] = username
            flash('Successfully Logged In')
        return redirect(url_for('index'))
    elif 'error' in request.args:
        flash(request.args['error_description'])
        return redirect(url_for('index'))
    else:
        return redirect(f'https://discord.com/api/oauth2/authorize?client_id={app.config["DISCORDCLIENT"]}&redirect_uri={app.config["DISCORDREDIRECTURI"]}&response_type=code&scope=identify%20email%20guilds.members.read')

@app.route('/logout')
def logout():
    """
    Logout page
    Clears session
    Returns to home
    """
    session.pop('loggedin', None)
    session.pop('username', None)
    flash('Successfully Logged Out')
    return redirect(url_for('index'))

@app.route('/account')
@login_required
def account():
    account = app.db.GetAccount(session['username'])
    if account:
        if 'state' in request.args:
            code = request.args['code']
            access_token, uid = Get_Access_Token(app.config['HFCLIENT'], app.config['HFSECRET'], code)
            if access_token:
                app.db.UpdateHF(account['username'], code, access_token, uid)
                flash(f'HF UID: {uid} Linked')
                account = app.db.GetAccount(session['username'])
                return render_template('account.html', account=account)
            else:
                flash('Error with HF API! Please try later.')

        name = account['username'].replace('#', '-')
        return render_template('account.html', account=account, name=name)
    else:
        flash('Error with account')
        return redirect(url_for('index'))

@app.route('/deleteemail')
@login_required
def deleteemail():
    app.db.DeleteEmail(session['username'])
    flash('Your email has been deleted successfully.')
    return redirect(url_for('account'))

@app.route('/deleteacc')
@login_required
def deleteacc():
    app.db.DeleteAccount(session['username'])
    flash('Account has been deleted successfully.')
    return redirect(url_for('logout'))

@app.route('/admin/deleteuseracc')
@login_required
@admin_required
def deleteuseracc():
    if 'id' in request.args:
        userid = request.args['id']
        app.db.AdminDeleteAccount(userid)
        flash('User has been deleted')
        return redirect(url_for('admin'))
    else:
        flash('Error deleting account.')
        redirect(url_for('admin'))

@app.route('/admin')
@login_required
@admin_required
def admin():
    account = app.db.GetAccount(session['username'])
    members = app.db.GetAllMembers()
    return render_template('admin/admin.html', account=account, members=members)

@app.route('/developer')
@login_required
@dev_required
def developer():
    account = app.db.GetAccount(session['username'])
    return render_template('admin/developer.html', account=account)