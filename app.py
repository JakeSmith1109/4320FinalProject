import sqlite3
import csv
from flask import Flask, render_template, request, url_for, flash, redirect, abort
# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

#flash  the secret key to secure sessions
app.config['SECRET_KEY'] = 'your secret key'

# use flask's app.route decorate to map the url to that function
@app.route("/")
def index():
    # add dropdown list options for main menu selection
    options = {'Admin Login': '/admin', 'Reserve a Seat': '/reservation'}

    return render_template('index.html', options=options)
    
@app.route('/reservation/', methods=('GET', 'POST'))
def reservation():
    # add dropdown list options for reservation (rows and columns)
    rows = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    seats = ['1', '2', '3', '4']
    return render_template('reservation.html', rows=rows, seats=seats)
        
@app.route('/admin/', methods=('GET', 'POST'))
def admin():

    return render_template('admin.html')

app.run(host="0.0.0.0", port=5002)