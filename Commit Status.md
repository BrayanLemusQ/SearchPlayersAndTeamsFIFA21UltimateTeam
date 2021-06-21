# Commit Purpose
Read the players whose name contains a specific string value and send them as a response. Any query creates a new table where the players that match the searched name are saved into a table  with multiple pages, each page contains maximum 10 items.

## Operation

***Run the flask app by typing the following line:***

    flask run


## Changes made compared to the previous one
- `CreatePlayersTableByTeam` function was changed to `CreatePlayersTable` in order to create a table whether the player is searched by name or by team
- `FindPlayersByTeam` function was changed to `FindPlayersByPage` given that the consulted table only store the desired information.
- Creation of `AquireURLParameters` to read the information about partial player name, search order and search page that comes with the URL by the time the request is made.
- `CreatePlayersResponse` function was defined to create the response message taking into account if the search is carried out by name or by equipment.
- Definition of `"/api/v1/players` route in order to search the players whose name contains a specific string value and send them as a response

## Files and Folders
### Modified files and folders

#### - routes.py
- `writeDataToTable` function was changed so it can store information either in the `fut21information` table or `teamplayerstable` table.
- `CreatePlayersTableByTeam` function was changed to `CreatePlayersTable` in order to store the information of each player that belongs to the consulted team or  whose name contains a specific string value, in addition depending of the amount of players, the information is saved with a page number that increments every time that 10 players has been stored in the page. This function deletes the `teamplayerstable` table everytime is called to store new data and ignore the above data.
  - The `function` receive a `list` data that must contain the value consulted in the first position, and the consult type in the second condition (**"By Team** or **By Player**)
  - The `function` returns a `boolean` data that indicates if the table was created or not.
- `FindPlayersByTeam` function was changed to `FindPlayersByPage` in order to explore the `teamplayerstable` table and select the players according to a specific page number.
    - The function receive an `integer` data that must contain the page number consulted
    - This `function` returns a `list` with the founded players according to the data received 
  - `CreatePlayersResponse` function was created extracting the code portion of `"/team"` route that was in charge of creating the response data. The changed was made to reuse the code when the search is by name or by team.
    - The function receive a list that contains the following data in the same order as it is named:
      - `list` that contains all the information read from a specific table.
      - `int` that contains the page number
      - `string` that contains the search type (**"By Team** or **By Player**))
  - `AquireURLParameters` function was created to read the information about partial player name, search order and search page that comes with the URL by the time the request is made.
    - This function does not receive any value
    - The `function` returns a `list` that contains **partial player name, search order and search page** 
  - `"/api/v1/players"` route was created route in order to search the players whose name contains a specific string value and send them as a response