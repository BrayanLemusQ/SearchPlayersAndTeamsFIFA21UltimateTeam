from flask import Flask
from mysql.connector import connection, cursor
import mysql.connector

app = Flask(__name__)   
app.secret_key = "appLogin"

connection = mysql.connector.connect(host="localhost", user="apifutadmin    ", password="admin")


@app.route("/")
def index():
    cursor = connection.cursor()
    query = "CREATE DATABASE IF NOT EXISTS apifut_database"
    cursor.execute(query)
    cursor.execute("DROP DATABASE IF EXISTS tempdb")
    cursor.execute("SHOW DATABASES")
    database_exists = False
    for database_name in cursor:
        print(database_name[0])
        if database_name[0]=="apifut_database": database_exists = True
    if database_exists == True:
        return "The database EXISTS"
    else:
        return "The database DOES NOT exist"