from flask import Flask

app = Flask(__name__)   
app.secret_key = "appLogin"
from config_database import *
from routes import *

if __name__=="main":
    app.run(debug=True)