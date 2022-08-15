from app import app
from dotenv import load_dotenv
import os

load_dotenv()

app.debug = os.getenv('DEBUG')
app.config['ENVIRONMENT'] = os.getenv('ENVIRONMENT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MYSQLHOST'] = os.getenv('MYSQLHOST')
app.config['MYSQLUSER'] = os.getenv('MYSQLUSER')
app.config['MYSQLPASS'] = os.getenv('MYSQLPASS')
app.config['MYSQLDB'] = os.getenv('MYSQLDB')

from app.database import MySQL

# Initialize Our DB
app.db = MySQL(app.config['MYSQLHOST'], app.config['MYSQLUSER'], app.config['MYSQLPASS'], app.config['MYSQLDB'])