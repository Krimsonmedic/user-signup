from flask import Flask, request, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-5" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <title>Validation Example</title>
    <link rel="stylesheet" href="/static/app.css" />
  </head>
  <body>
"""

welcomeMessage = """
<h1>Welcome to my super cool page!</h1>
<a href="/register">Register</a> """


page_footer = """
 </body>
</html>
"""

# a registration form


@app.route("/register", methods=['POST'])
def register():
    username = cgi.escape(request.form['username'])
    password = cgi.escape(request.form['password'])
    password2 = cgi.escape(request.form['password2'])
    email = cgi.escape(request.form['email'])

    usernameError =""
    passwordError = ""
    password2Error =""
    emailError = ""

    if not username:
        print("no username")
        usernameError = "Username is required"
    if len(username) < 3 or len(username) > 20:
        usernameError = "Usernames must be between 3 and 20 characters"
    for char in username:
        if char == " ":
            usernameError = "usernames cannot contain spaces"
    if not password:
        passwordError = "Password is required"
    elif len(password) < 3 or len(password) > 20:
        passwordError = "Password must be at least 5 characters long, and no more than 20"
    else:
        hasNumber = False
        for char in password:
            if char.isdigit():
                hasNumber = True
        if not hasNumber:
            passwordError = "Password must contain a number"
        for char in password:
            if char == " ":
                passwordError = "password cant contain a space"
    if password  != password2:
        password2Error = "Password 2 must match password"
    
    if email != "":
        if len(email) < 3:
            emailError= "Email must be at least 3 characters long"

        else:
            for char in email:
                if char == " ":
                    emailError = "There are no spaces in an email"
            hasAt = 0
            for char in email:
                if char == "@":
                    hasAt +=1

            if hasAt != 1 :
                emailError = "Email's must contain a single @"
            hasPeriod = 0
            for char in email:
                if char == ".":
                    hasPeriod += 1

            if hasPeriod !=1:
                emailError = "Email's must contain a single . "


             

    

    if usernameError or passwordError or password2Error or emailError:
        print("there was an error!")
        varlist=[username, usernameError, 
        password, passwordError, password2, password2Error]
        return render_template('registration.html', username= username, email= email, var1 =usernameError, var2 =passwordError, var3 = password2Error, emailError = emailError  )

    return "Thanks for registering, " + username


@app.route("/")
def index():
    # build the response string
    content = welcomeMessage + page_footer
    return render_template('base.html') +content

@app.route("/register", methods=['GET'])
def register_page():
    # build the response string
    
    return render_template('registration.html')

app.run()

## Cross Site scripting
# <script>alert("HEHEHEHE")</script>