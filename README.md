# SearchPlayersAndTeamsFIFA21UltimateTeam
API that extracts information from FUT21 API dataset to find players and teams.


## Operation
Add the following user with all the priviliges in mysql server:  

    HOST : 'localhost'
    USER : 'apifutadmin'
    PASSOWORD : 'admin' 

The database `apifut_database` where the data would be stored is created automatically.

Make sure the virtual environment is running. The word `(env)` should be at the beginning of the command line on the terminal. 

    (env) PS C:\Desktop\Online-Roulette> 

If the virtual environment is not running type the following line on the terminal

    .\env\Scripts\Activate.ps1

***Run the flask app by typing the following line:***

    flask run

### **¬ Use the */* endpoint** to read all the information in the API FUT 21 and store it into the database `apifut_database` in the table `fut21information`
This route should be called by a GET method request. If the process is complete succesfully a **"data Collected"** message will be shown.

### **¬ Use the */team* endpoint** to search for all the players in a specific team 

Make sure to use a `POST REQUEST` with the following json structure:

    {
        "Name": valid_team_name
        "Page": page_number
    }
The `page_numer` should be `int`

The only valid keys in the `JSON` structure are `Name` and `Page`, if the request does not brings this data, the endpoint will respond:

    {
        "Update": "Failed",
        "error": "Invalid Key",
        "response": 400
    }

The response to a succesful team searching should look like this:

    {
        “Page”: 1,
        “totalPages: 2
        “Items”: 10,
        “totalItems”:20,
        “Players” : [
            { name: “Marcelo”, “position”: “LB”, “nation” : “Brazil” },
            ...
            ]
    }

### **¬ Use the *//api/v1/players* endpoint** to search for all the players whose names contains a specific string
Make sure to use a `GET REQUEST` with the following URL structure:

    /api/v1/players?search=partial_player_name&order=desired_order&page=page_number

The `partial_player_name` could be any string, the code will search for any player name that match. If this parameter is not send in the URL, the API will response with all the players in the database.

If the sended string does not match with any player the response will be:

    {
        "Search": "Failed",
        "error": "Player Not found",
        "response": 400
    }

The `desired_order` should be either ***asc*** or ***desc*** other wise the response information would be shown in **alphabetical ascending order**. Please send ***desc*** to organize the information in **alphabetical descending order**

The response to a succesful player searching should look like this:

    {
        “Page”: 1,
        “totalPages: 1
        “Items”: 10,
        “totalItems”:10,
        “Players” : [
            { name: “Cristiano Ronaldo”, “position”: “ST”, “nation” : “Portugal” , “team”: “Juventus”},
            ...
            ]
    }