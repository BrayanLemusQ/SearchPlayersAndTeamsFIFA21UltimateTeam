# Commit Purpose
This commit purpose is to explain the functionality of the SearchPlayersAndTeamsFiFA21UltimateTeam API. In addition an error message was added to the `/team` route that will be shown when receiving an invalid key, and a new condition was added to the `AquireURLParameters` function to fix the error produced when the search parameter is not sent when calling the endpoint

## Operation

***Run the flask app by typing the following line:***

    flask run


## Changes made compared to the previous one
- `Readme` file was completed with the explanation of the code functionality.
- Error message was added to the `/team` route that will be shown when receiving an invalid key
- New condition was added to the `AquireURLParameters` function to fix the error produced when the search parameter is not sent when calling the endpoint

## Files and Folders
### Modified files and folders

#### - routes.py
- `AquireURLParameters` function was modified, if the parameter search is not received in the URL the returned value for `partial_player_name` will be an empty string, that will cause that the API response with all the players stored in the database.
- `/team` route was modified to validate if the `POST method request` used brings the valid keys `"Name"` and `"Page"`