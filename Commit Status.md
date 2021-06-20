# Commit Purpose
Read the players from a specific team and send them as a response. Any query creates a new table where the players that correspond to that specific team are saved into multiple pages, each pages contains maximum 10 items.

## Operation

***Run the flask app by typing the following line:***

    flask run


## Changes made compared to the previous one
- Creation of `teamplayerstable` table to store the players that belongs to the consulted team
- Definition of `"/team` route to consult the players that belongs to a specific team

## Files and Folders
### Modified files and folders
#### - config_database.py
- Creation of `teamplayerstable` table with the same columns of `fut21information` to store the players that belongs to the consulted team

#### - routes.py
- `writeDataToTable` function was changed so it can store information either in the `fut21information` table or `teamplayerstable` table.
- `CreatePlayersTableByTeam` function was created to store the information of each player that belongs to the consulted team, in addition depending of the amount of players, the information is saved with a page number that increments every time that 10 players has been stored in the page. This function deletes the `teamplayerstable` table everytime is called to store new data and ignore the above data.
  - The `function` receive a `string` data that must contain the name of the team consulted
  - The `function` returns a `boolean` data that indicates if the team exist or not.
- `FindPlayersByTeam` function was created to explore the `teamplayerstable` table and select the players according to a specific page number.
    - The function receive a `string` data that must contain the name of the team consulted and an `integer` data that must contain the page number consulted
    - This `function` returns a `list` with the founded players according to the data received 
  - `FindMaxValue` function was created to find the maximun number either in the `Id` Column or the `Page` Column in the table `teamplayerstable`
    - The `function` receive a `string` that must contain the name of the column where the maximun is requested
    - The `function` returns an `integer` with the maximum value stored
  - `"/team"` route was created to explore the information readed from the API FIFA 21 Ultimate Team and respond the players that belongs to a specific team.