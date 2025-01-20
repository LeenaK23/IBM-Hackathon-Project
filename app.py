from flask import Flask, render_template, request, redirect, url_for, flash
import ibm_db
import hashlib
import secrets
app = Flask(__name__)
app.secret_key = secrets.token_hex(32)

# IBM Db2 Connection string
db2_connection_string = "DATABASE=bludb;HOSTNAME=0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31198;PROTOCOL=TCPIP;UID=qsj67798;PWD=LKc0qT2omrUoA6qm;SECURITY=SSL"




# Route for displaying the signup page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get the user inputs from the signup form
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
        # Create connection to Db2
        conn = ibm_db.connect(db2_connection_string, '', '')
        if conn:
            # Check if the username already exists
            check_sql = f"SELECT * FROM Users WHERE Username = ?"
            stmt = ibm_db.prepare(conn, check_sql)
            ibm_db.bind_param(stmt, 1, username)
            ibm_db.execute(stmt)
            result = ibm_db.fetch_assoc(stmt)
            
            if result:
                flash("Username already exists!", "danger")
                return redirect(url_for('signup'))

            # Insert new user into the User table
            insert_sql = f"INSERT INTO Users (username, passw) VALUES (?, ?)"
            stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(stmt, 1, username)
            ibm_db.bind_param(stmt, 2, hashed_password)
            ibm_db.execute(stmt)

            flash("Signup successful! Please log in.", "success")
            return redirect(url_for('login'))
        else:
            flash("Database connection failed!", "danger")
            return redirect(url_for('signup'))

    return render_template('signup.html')


# Route for displaying the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the user inputs from the login form
        username = request.form['username']
        password = request.form['password']
        hashed_password = hashlib.sha256(password.encode()).hexdigest()  # Hash the password
        
        # Create connection to Db2
        conn = ibm_db.connect(db2_connection_string, '', '')
        if conn:
            # Check if the username and password match
            check_sql = f"SELECT * FROM Users WHERE username = ? AND passw = ?"
            stmt = ibm_db.prepare(conn, check_sql)
            ibm_db.bind_param(stmt, 1, username)
            ibm_db.bind_param(stmt, 2, hashed_password)
            ibm_db.execute(stmt)
            result = ibm_db.fetch_assoc(stmt)
            
            if result:
                flash("Login successful!", "success")
                return redirect(url_for('main'))  # Redirect to a dashboard or home page
            else:
                flash("Invalid username or password!", "danger")
                return redirect(url_for('login'))
        else:
            flash("Database connection failed!", "danger")
            return redirect(url_for('login'))
    
    return render_template('login.html')


# Route for the dashboard or home page after login
@app.route('/')
def initial():
    return render_template('welcome.html')

@app.route('/main')
def main():
    user_details = {
        "username": "JohnDoe"  # Replace with actual session data
    }
    return render_template('main.html', user=user_details)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == '__main__':
    app.run(debug=True)
