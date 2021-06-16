from flask import Flask
from mysql.connector import connection, cursor
import mysql.connector

app = Flask(__name__)   
app.secret_key = "appLogin"

connection = mysql.connector.connect(host="localhost", user="apifutadmin    ", password="admin")
cursor = connection.cursor()
query = "CREATE DATABASE IF NOT EXISTS apifut_database"
cursor.execute(query)
cursor.close()
connection = mysql.connector.connect(host="localhost", user="apifutadmin    ", password="admin", database="apifut_database")


@app.route("/")
def index():
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS fut21information"
    cursor.execute(query)
    cursor.execute("CREATE TABLE IF NOT EXISTS fut21information (Id int unsigned NOT NULL, PlayerName char(20) DEFAULT NULL, Position char(20) DEFAULT NULL, Nationality char(20) DEFAULT NULL, Team char(20) DEFAULT NULL, Page int DEFAULT 1)")
    query = "INSERT INTO fut21information(Id, PlayerName, Position, Nationality, Team) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query,(str(1),"Cristiano", "Delantero", "Portugal", "Real Madrid"))
    connection.commit()
    cursor.execute("SHOW TABLES")
    table_exists = False
    for table_name in cursor:
        print(table_name[0])
        if table_name[0]=="fut21information": table_exists = True
    if table_exists == True:
        return "The table EXISTS"
    else:
        return "The table DOES NOT exist"