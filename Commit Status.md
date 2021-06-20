# Commit Purpose
Reading information from API Fut FIFA 21 Ultimate Team and store the information into the `apifut_database` 

## Operation

***Run the flask app by typing the following line:***

    flask run


## Changes made compared to the previous one
- Installation of HTTP Library `Request`
- Installation of `jsonify` python script
- The code dedicated to the definition of the route `"/"` was moved from `app.py` to a new file named `config_database.py`

## Files and Folders
### Created files and folders
#### - config_database.py
- Addition of `PlayerCommonName` column to the `fut21information` given that some players comes with a commmon name and theyre full name, so this data is stored to be able to search later either by the full name or by the common name.

#### - routes.py
- `writeDataToTable` function is created to store a single data into the `fut21information` table. The function receive a list type data that must contains `playername`, `common_playername`, `player_position`, `player_nationality`, `player_club`, `page`
- `readInformation` function is created to read the information from API Fut FIFA 21 Ultimate Team, this function reads the API to adquire the amount of pages, and make the request to all the pages.
