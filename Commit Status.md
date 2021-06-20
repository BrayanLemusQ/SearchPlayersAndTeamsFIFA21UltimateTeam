# Commit Purpose
Creation of files to database configuration and routes definition in order to organize the code and separate functionalities

## Operation

***Run the flask app by typing the following line:***

    flask run

Call the route *"/"* and verify that the table ***fut21information*** exists 

## Changes made compared to the previous one
- The code dedicated to table `fut21information` Creation was moved from `app.py` to a new file named `config_database.py`
- The code dedicated to the definition of the route `"/"` was moved from `app.py` to a new file named `config_database.py`

## Files and Folders
### Created files and folders
#### - config_database.py
- Database existence verification
- Connection to `apifut_database` database
- Table `fut21information`elimination and creation of a new `fut21information`tables

#### - routes.py
- `"/"` route definition
- Value [1,"Cristiano", "Delantero", "Portugal", "Real Madrid", 1] addition to `fut21information` table
