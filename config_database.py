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
query = "CREATE TABLE IF NOT EXISTS fut21information (Id int unsigned NOT NULL AUTO_INCREMENT, PlayerName char(60) DEFAULT NULL, PlayerCommonName char(60) DEFAULT NULL, Position char(30) DEFAULT NULL, Nationality char(50) DEFAULT NULL, Team char(50) DEFAULT NULL, Page int DEFAULT 1, PRIMARY KEY(Id))"
cursor.execute(query)
query = "CREATE TABLE IF NOT EXISTS teamplayerstable (Id int unsigned NOT NULL AUTO_INCREMENT, PlayerName char(60) DEFAULT NULL, PlayerCommonName char(60) DEFAULT NULL, Position char(30) DEFAULT NULL, Nationality char(50) DEFAULT NULL, Team char(50) DEFAULT NULL, Page int DEFAULT 1, PRIMARY KEY(Id))"
cursor.execute(query)
cursor.close()

    