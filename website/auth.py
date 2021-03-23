from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html", boolean=False)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email mora biti veci od 4 karaktera", category="error")
        elif len(firstName) < 2:
            flash("Ime mora biti veci od 1 karaktera", category="error")
        elif password1 != password2:
            flash("Šifre se ne poklapaju", category="error")
        elif len(password1) < 7:
            flash("Šifra mora biti veci od 7 karaktera", category="error")
        else:
            flash("Kreirano uspješno!", category="success")

    return render_template("sign_up.html")
