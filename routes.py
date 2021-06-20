from app import app
from mysql.connector import connection, cursor
from flask import jsonify, request
import mysql.connector
import requests


connection = mysql.connector.connect(host="localhost", user="apifutadmin", password="admin", database="apifut_database")

def readInformation():
    base_url = "https://www.easports.com/fifa/ultimate-team/api/fut/item?page={}"
    url = base_url.format(1)
    players_data = requests.get(url).json()
    number_of_pages = players_data["totalPages"]
    for page in range(3):
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
            writeDataToTable(player_data,"fut21information")

def CreatePlayersTableByTeam(team):
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS teamplayerstable"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS teamplayerstable (Id int unsigned NOT NULL AUTO_INCREMENT, PlayerName char(30) DEFAULT NULL, PlayerCommonName char(30) DEFAULT NULL, Position char(30) DEFAULT NULL, Nationality char(20) DEFAULT NULL, Team char(30) DEFAULT NULL, Page int DEFAULT 1, PRIMARY KEY(Id))"
    cursor.execute(query)
    query = "SELECT * FROM fut21information WHERE Team = %s" 
    cursor.execute(query,[team])
    players_found = cursor.fetchall()
    team_found = False
    if players_found != []:
        items = 0
        for player_found in players_found:
            items+=1
            common_playername = player_found[1]
            playername = player_found[2]
            player_position = player_found[3]
            player_nationality = player_found[4]
            player_club = player_found[5]
            if items%10 == 0:page = items//10
            else: page = items//10 + 1 
            player_data = [playername, common_playername, player_position, player_nationality, player_club, page]
            writeDataToTable(player_data,"teamplayerstable")
        team_found = True
    cursor.close()

    return team_found

def writeDataToTable(player_data, table_name):
    cursor = connection.cursor()
    if table_name == "fut21information":
        query = "INSERT INTO fut21information(PlayerName, PlayerCommonName, Position, Nationality, Team, Page) VALUES (%s, %s, %s, %s, %s, %s)"
    if table_name == "teamplayerstable":
        query = "INSERT INTO teamplayerstable(PlayerName, PlayerCommonName, Position, Nationality, Team, Page) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(player_data))
    connection.commit()
    cursor.close()

def FindPlayersByTeam(team,page_number):
    cursor = connection.cursor()
    query = "SELECT * FROM teamplayerstable WHERE Team = %s AND Page = %s"
    cursor.execute(query,[team,page_number]) 
    players_found = cursor.fetchall()
    cursor.close()

    return players_found

def FindMaxValue(value):
    cursor = connection.cursor()
    if value == "Id": query = "SELECT MAX(Id) AS maximum FROM teamplayerstable"
    if value == "Page": query = "SELECT MAX(Page) AS maximum FROM teamplayerstable"
    cursor.execute(query)
    values = cursor.fetchall()
    max_value = values[0][0]
    cursor.close()

    return max_value

@app.route("/", methods=["GET"])
def index():
    cursor = connection.cursor()
    query = "INSERT INTO fut21information(Id, PlayerName, PlayerCommonName, Position, Nationality, Team) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(str(1),"Cristiano", "Cristiano Ronaldo", "Delantero", "Portugal", "Real Madrid"))
    connection.commit()
    data = readInformation()
    return "data Collected"

@app.route("/team", methods=["POST"])
def team():
    request_json_data = request.json
    team_name = request_json_data["Name"]
    page_number = request_json_data["Page"]
    team_found = CreatePlayersTableByTeam(team_name)
    players_found = FindPlayersByTeam(team_name,page_number)
    player_data = {}
    player_response = {}    
    if team_found:
        number_of_players = FindMaxValue("Id")
        number_of_pages = FindMaxValue("Page")
        players = [None]*len(players_found)
        player_number=0
        for player_found in players_found:
            player_data["name"] = player_found[1]
            player_data["position"] = player_found[3]
            player_data["nation"] = player_found[4]
            players[player_number]=player_data
            player_data = {}
            player_number+=1
        player_response["page"] = page_number
        player_response["totalPages"] = number_of_pages
        player_response["Items"] = player_number
        player_response["totalItems"] = number_of_players
        player_response["Players"] = players

        return jsonify(player_response)
    else:

        return jsonify({'response':400,'Search':"Failed",'error':"Team Not found"})   


