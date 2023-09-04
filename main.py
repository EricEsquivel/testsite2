from flask import Flask, flash, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
import jsonstuff

app = Flask(__name__)
app.config["SECRET_KEY"] = "Supercalifragilisticexpialidocious"

######### Default page is the login, and it will run a check in accounts.json to make sure account exists #########
@app.route("/", methods = ["GET", "POST"])
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if len(username) == 0:
            flash("You need to type in a username!", category="error")
        elif len(password) == 0:
            flash("You need to type in a password!", category="error")
        else:
            loginaccount = {"username": username, "password": password}
            if jsonstuff.logincheck(loginaccount) == "logged in":
                flash(f"Signed in as {username}!", category="success")
            else:
                flash("Invalid credentials!", category="error")
    return render_template("home.html")


######### Register route for homepage, and it will runa check in accounts.json to make sure account doesn't exist already #########
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if len(username) == 0:
            flash("You need to type in a username!", category="error")
        elif len(password) == 0:
            flash("You need to type in a password!", category="error")
        else:
            newaccount = {"username": username, "password": password}
            if jsonstuff.registercheck(newaccount) == "success":
                flash("Account registered!", category="success")
            else:
                flash("That username already exists!", category="failure")
    return render_template("register.html", boolean=True)


######### Run in debug mode so that when you make changes, it auto updates the server without having to restart #########
if __name__ == "__main__":
    app.run(debug=True)