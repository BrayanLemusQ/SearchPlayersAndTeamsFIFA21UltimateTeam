# Commit Purpose
This commit purpose is to add the functionality of ordering the response information ascending or descending by the time a search by name is executed. In addition the `readInformation` function was modified so the API can read all the pages in API FUT 21

## Operation

***Run the flask app by typing the following line:***

    flask run


## Changes made compared to the previous one
- `CreatePlayersTable` was modified to received the ordering value as a third list parameter
- `"/team` route was modified to send an empty string when the `CreatePlayersTable` function is called
- `"/api/v1/players"` route was modified to send a string with the order readed from the request when the `CreatePlayersTable` function is called

## Files and Folders
### Modified files and folders

#### - routes.py
- `CreatePlayersTable` 
  - The `function` receive a `list` data that must contain the value consulted in the first position, the consult type in the second condition (**"By Team** or **By Player**) and the ordering information `string` in the third position (**"asc** or **desc**).
    - The `function` returns a `boolean` data that indicates if the table was created or not.
  - `"/api/v1/players"` route was modified to route in order to send a string with the order readed from the request when the `CreatePlayersTable` function is called
  - `"/team` route was modified to send an empty string when the `CreatePlayersTable` function is called
  - `readInformation` function was modified so the API can read all the pages in API FUT 21
  - `"/"` route was modified to delete old information and aquire new information reading the API FUT 21  