from flask import Flask
from mysql.connector import connection, cursor
import mysql.connector

app = Flask(__name__)

if __name__=="main":
    app.run(debug=True)