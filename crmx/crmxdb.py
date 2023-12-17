import mysql.connector
from crmx.config_ini import *

config = con()

database = mysql.connector.connect(
    host="localhost",
    user = 'root',
    passwd = config['DEFAULT']['PASSWORD']
)

# prepare a cursor object
cursorObject = database.cursor()

# create database
cursorObject.execute('CREATE DATABASE IF NOT EXISTS crmxdb')
print('All Done')