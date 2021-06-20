import re
from app import app
from mysql.connector import connection, cursor
import mysql.connector
import requests
import jsonify

connection = mysql.connector.connect(host="localhost", user="apifutadmin", password="admin", database="apifut_database")

@app.route("/")
def index():
    cursor = connection.cursor()
    query = "INSERT INTO fut21information(Id, PlayerName, PlayerCommonName, Position, Nationality, Team) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(str(1),"Cristiano", "Cristiano Ronaldo", "Delantero", "Portugal", "Real Madrid"))
    connection.commit()
    data = readInformation()
    return "data Collected"

def readInformation():
    base_url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}"
    url = base_url.format(1)
    players_data = requests.get(url).json()
    
    print(players_data["totalPages"])
    number_of_pages = players_data["totalPages"]
    for page in range(5):
        url = base_url.format(page)
        players_data = requests.get(url).json()
        page = players_data["page"]
        print(players_data["page"])
        print(players_data["count"])
        for player in players_data["items"]:
            common_playername = player["commonName"]
            playername = player["firstName"]+" "+player["lastName"]
            player_position = player["positionFull"]
            player_nationality = player["nation"]["name"]
            player_club = player["club"]["name"]
            player_data = [playername, common_playername, player_position, player_nationality, player_club, page]
            writeDataToTable(player_data)

def writeDataToTable(player_data):
    cursor = connection.cursor()
    query = "INSERT INTO fut21information(PlayerName, PlayerCommonName, Position, Nationality, Team, Page) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(player_data))
    connection.commit()
    cursor.close()
