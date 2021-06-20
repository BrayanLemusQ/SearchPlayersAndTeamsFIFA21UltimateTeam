from app import app
from mysql.connector import connection, cursor
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="apifutadmin", password="admin", database="apifut_database")

@app.route("/")
def index():
    cursor = connection.cursor()
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