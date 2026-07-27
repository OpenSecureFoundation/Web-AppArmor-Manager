from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

app.secret_key = "apparmor_secret_key"

# Utilisateur de démonstration
USERNAME = "admin"
PASSWORD = "admin123"


@app.route("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():

    erreur = None

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:

            session["user"] = username

            return redirect(url_for("dashboard"))

        else:

            erreur = "Nom d'utilisateur ou mot de passe incorrect."

    return render_template("login.html", erreur=erreur)


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        utilisateur=session["user"]
    )


@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
