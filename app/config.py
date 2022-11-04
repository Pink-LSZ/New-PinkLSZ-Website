from app import app
import os

app.debug = True
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MYSQLHOST'] = os.getenv('MYSQLHOST')
app.config['MYSQLUSER'] = os.getenv('MYSQLUSER')
app.config['MYSQLPASS'] = os.getenv('MYSQLPASS')
app.config['MYSQLDB'] = os.getenv('MYSQLDB')
app.config['DISCORDCLIENT'] = os.getenv('DISCORDCLIENT')
app.config['DISCORDSECRET'] = os.getenv('DISCORDSECRET')
app.config['DISCORDREDIRECTURI'] = os.getenv('DISCORDREDIRECTURI')
app.config['HFCLIENT'] = os.getenv('HFCLIENT')
app.config['HFSECRET'] = os.getenv('HFSECRET')

from app.database import MySQL

# Initialize Our DB
app.db = MySQL(app.config['MYSQLHOST'], app.config['MYSQLUSER'], app.config['MYSQLPASS'], app.config['MYSQLDB'])

@app.context_processor
def inject_settings() -> dict:
    """
    Sets our global settings
    settings: Global settings from DB
    """
    settingsquery = app.db.query('SELECT * from settings', querytype='select', fetchall=False)
    settings = {
        'settings': settingsquery,
        'hf': {
            'secret':app.config['HFSECRET'],
            'client':app.config['HFCLIENT'],
        }
    }
    return settings