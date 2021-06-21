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
    for page in range(number_of_pages+1):
        url = base_url.format(page)
        players_data = requests.get(url).json()
        page = players_data["page"]
        print(players_data["page"])
        for player in players_data["items"]:
            common_playername = player["commonName"]
            playername = player["firstName"]+" "+player["lastName"]
            player_position = player["positionFull"]
            player_nationality = player["nation"]["name"]
            player_club = player["club"]["name"]
            player_data = [playername, common_playername, player_position, player_nationality, player_club, page]
            writeDataToTable(player_data,"fut21information")

def CreatePlayersTable(search_data):
    search_value = search_data[0]
    search_type = search_data[1]
    search_order = search_data[2]
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS teamplayerstable"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS teamplayerstable (Id int unsigned NOT NULL AUTO_INCREMENT, PlayerName char(60) DEFAULT NULL, PlayerCommonName char(60) DEFAULT NULL, Position char(30) DEFAULT NULL, Nationality char(50) DEFAULT NULL, Team char(50) DEFAULT NULL, Page int DEFAULT 1, PRIMARY KEY(Id))"
    cursor.execute(query)
    if search_type == "By Team": query = "SELECT * FROM fut21information WHERE Team = %s"        
    if search_type == "By Player": 
        if search_order == "asc" : query = "SELECT * from fut21information where PlayerName LIKE %s order by PlayerName"
        elif search_order == "desc" : query = "SELECT * from fut21information where PlayerName LIKE %s order by PlayerName desc"
    cursor.execute(query,[search_value])    
    players_found = cursor.fetchall()
    team_found = False
    if players_found != []:
        items = 0
        for player_found in players_found:
            items+=1
            playername = player_found[1]
            common_playername = player_found[2]
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

def CreatePlayersResponse(response_data):
    players_found = response_data[0]
    page_number = response_data[1]
    search_type = response_data[2]
    player_data = {}
    player_response = {}
    number_of_players = FindMaxValue("Id")
    number_of_pages = FindMaxValue("Page")
    players = [None]*len(players_found)
    player_number=0
    for player_found in players_found:
        player_data["name"] = player_found[1]
        player_data["position"] = player_found[3]
        player_data["nation"] = player_found[4]
        if search_type == "By Player": player_data["team"] = player_found[5]
        players[player_number]=player_data
        player_data = {}
        player_number+=1
    player_response["page"] = page_number
    player_response["totalPages"] = number_of_pages
    player_response["Items"] = player_number
    player_response["totalItems"] = number_of_players
    player_response["Players"] = players

    return player_response

def writeDataToTable(player_data, table_name):
    cursor = connection.cursor()
    if table_name == "fut21information":
        query = "INSERT INTO fut21information(PlayerName, PlayerCommonName, Position, Nationality, Team, Page) VALUES (%s, %s, %s, %s, %s, %s)"
    if table_name == "teamplayerstable":
        query = "INSERT INTO teamplayerstable(PlayerName, PlayerCommonName, Position, Nationality, Team, Page) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query,(player_data))
    connection.commit()
    cursor.close()

def FindPlayersByPage(page_number):
    cursor = connection.cursor()
    query = "SELECT * FROM teamplayerstable WHERE Page = %s"
    cursor.execute(query,[page_number]) 
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

def AquireURLParameters():
    partial_player_name = request.args.get("search")
    search_order = request.args.get("order")
    if search_order != "asc" and search_order != "desc": search_order = "asc"    
    search_page = request.args.get("page")
    if search_page == None: search_page = 1        
    elif search_page.isdigit():
        search_page = int(search_page) 
        if search_page<=0: search_page = 1
    else: search_page = 1
    parameters = [partial_player_name,search_order,search_page]

    return parameters

@app.route("/", methods=["GET"])
def index():
    cursor = connection.cursor()
    query = "DROP TABLE IF EXISTS fut21information"
    cursor.execute(query)
    query = "CREATE TABLE IF NOT EXISTS fut21information (Id int unsigned NOT NULL AUTO_INCREMENT, PlayerName char(60) DEFAULT NULL, PlayerCommonName char(60) DEFAULT NULL, Position char(30) DEFAULT NULL, Nationality char(50) DEFAULT NULL, Team char(50) DEFAULT NULL, Page int DEFAULT 1, PRIMARY KEY(Id))"
    cursor.execute(query)
    data = readInformation()
    return "data Collected"

@app.route("/team", methods=["POST"])
def team():
    request_json_data = request.json
    team_name = request_json_data["Name"]
    page_number = request_json_data["Page"]
    team_found = CreatePlayersTable([team_name, "By Team", ""])
    players_found = FindPlayersByPage(page_number)
    player_response = {}    
    if team_found:
        player_response = CreatePlayersResponse([players_found,page_number,"By Team"])
        return jsonify(player_response)
    else:
        return jsonify({'response':400,'Search':"Failed",'error':"Team Not found"})   

@app.route("/api/v1/players", methods=["GET"])
def SearchPlayers():
    [partial_player_name, search_order, page_number] = AquireURLParameters()
    partial_player_name ="%"+partial_player_name+"%" 
    team_found = CreatePlayersTable([partial_player_name, "By Player", search_order])
    players_found = FindPlayersByPage(page_number)
    player_response = {}    
    if team_found:
        player_response = CreatePlayersResponse([players_found,page_number,"By Player"])
        return jsonify(player_response)
    else:
        return jsonify({'response':400,'Search':"Failed",'error':"Team Not found"}) 




