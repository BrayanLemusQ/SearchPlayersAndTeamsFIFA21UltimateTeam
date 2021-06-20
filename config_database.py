from mysql.connector import connection, cursor
import mysql.connector

connection = mysql.connector.connect(host="localhost", user="apifutadmin", password="admin")
cursor = connection.cursor()
query = "CREATE DATABASE IF NOT EXISTS apifut_database"
cursor.execute(query)
cursor.execute("SHOW DATABASES")
database_exists = False
for database_name in cursor:
    if database_name[0]=="apifut_database": database_exists = True
if database_exists == True:
    print("The database EXISTS")
else:
    print("The database DOES NOT exist")
connection = mysql.connector.connect(host="localhost", user="apifutadmin", password="admin", database="apifut_database")
cursor = connection.cursor()
query = "DROP TABLE IF EXISTS fut21information"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS fut21information (Id int unsigned NOT NULL, PlayerName char(20) DEFAULT NULL, Position char(20) DEFAULT NULL, Nationality char(20) DEFAULT NULL, Team char(20) DEFAULT NULL, Page int DEFAULT 1)"
cursor.execute(query)
cursor.close()

    