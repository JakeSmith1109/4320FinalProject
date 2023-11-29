from flask import Flask, render_template, request, url_for, flash, redirect

# make a Flask application object called app
app = Flask(__name__)
app.config["DEBUG"] = True

# flash the secret key to secure sessions
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
    if request.method == 'POST':
        # get the entered username and password from the form
        entered_username = request.form.get('username')
        print(entered_username)
        entered_password = request.form.get('password')
        print(entered_password)

        # check the credentials against data in the passcodes.txt file
        if check_credentials(entered_username, entered_password):
            # credentials are valid, flash a success message and redirect to the same page
            flash("Login Successful!", 'success')
            print("Login Successful!")  # Add this for debugging
            return redirect(url_for('admin'))
        else:
            # credentials are invalid, flash an error message and redirect to the same page
            flash("Login Failed! Please try again.", 'error')
            print("Login Failed!")  # Add this for debugging
            return redirect(url_for('admin'))
    else:
        # this handles the initial GET request, render the page without a message
        return render_template('admin.html')

def check_credentials(entered_username, entered_password):
    # Read data from the passcodes.txt file and check against entered credentials
    with open('passcodes.txt', 'r') as file:
        for line in file:
            username, password = map(str.strip, line.split(','))
            print(f"Checking: {username}, {password}")
            if entered_username == username and entered_password == password:
                return True
    return False

app.run(host="0.0.0.0", port=5002)