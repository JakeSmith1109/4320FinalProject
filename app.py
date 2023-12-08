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
    rows = ["Choose a Row", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    seats = ["Choose a Seat", '1', '2', '3', '4']

    # Get the path to the text file containing seating data
    file_path = '4320FinalProject/reservations.txt'  # Replace with the actual path

    # Create the seat chart
    seat_chart_data = create_seat_chart('4320FinalProject/reservations.txt')

    return render_template('reservation.html', rows=rows, seats=seats, file_path = file_path, seat_chart=seat_chart_data)

        
@app.route('/admin', methods=('GET', 'POST'))
def admin():
    if request.method == 'POST':
        # get the entered username and password from the form
        entered_username = request.form.get('username')
        print(entered_username)
        entered_password = request.form.get('password')
        print(entered_password)

        # check the credentials against data in the passcodes.txt file
        if check_credentials(entered_username, entered_password):
            # if credentials are valid, flash a success message and redirect to the same page
            flash("Login Successful!", 'success')

            # add dropdown list options for reservation (rows and columns)
            rows = ["Choose a Row", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
            seats = ["Choose a Seat", '1', '2', '3', '4']

            # Get the path to the text file containing seating data
            file_path = '4320FinalProject/reservations.txt'  # Replace with the actual path

            # Create the seat chart
            seat_chart_data = create_seat_chart('4320FinalProject/reservations.txt')

            # debugging code here: print("Login Successful!")
            return render_template('adminHome.html', rows=rows, seats=seats, file_path = file_path, seat_chart=seat_chart_data)  # Replace with the actual template for the admin home page
        else:
            # if credentials are invalid, flash an error message and redirect to the same page
            flash("Login Failed! Please try again.", 'error')
            # debugging code here: print("Login Failed!")
            return redirect(url_for('/admin'))
    else:
        # this handles the initial GET request, render the page without a message
        return render_template('/admin.html')

def check_credentials(entered_username, entered_password):
    # read data from the passcodes.txt file and check against entered credentials
    with open('4320FinalProject/passcodes.txt', 'r') as file:
        for line in file:
            username, password = map(str.strip, line.split(','))
            # debugging code here: print(f"Checking: {username}, {password}")
            if entered_username == username and entered_password == password:
                return True
    return False


def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for _ in range(12)]
    return cost_matrix


def create_seat_chart(file_path):
    seat_chart = [['o' for _ in range(4)] for _ in range(12)]

    with open(file_path, 'r') as file:
        for line in file:
            _, row, seat, _ = line.strip().split(', ')
            row, seat = int(row), int(seat)
            seat_chart[row][seat] = 'x'

    return seat_chart


@app.route('/admin')
def adminHome():
    
    # add dropdown list options for reservation (rows and columns)
    rows = ["Choose a Row", '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    seats = ["Choose a Seat", '1', '2', '3', '4']

    # Get the path to the text file containing seating data
    file_path = '4320FinalProject/reservations.txt'  # Replace with the actual path

    # Create the seat chart
    seat_chart_data = create_seat_chart('4320FinalProject/reservations.txt')

    return render_template('adminHome.html', rows=rows, seats=seats, file_path=file_path, seat_chart=seat_chart_data)

app.run(host="0.0.0.0", port=5002)