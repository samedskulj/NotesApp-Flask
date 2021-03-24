from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Ulogovan uspješno!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))

            else:
                flash("Netačni podaci, pokušajte ponovo!", category='error')
        else:
            flash("Email ne postoji.", category='error')

    return render_template("login.html", user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/signup", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        firstName = request.form.get("firstName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email vec postoji.', category='error')
        elif len(email) < 4:
            flash("Email mora biti veci od 4 karaktera", category="error")
        elif len(firstName) < 2:
            flash("Ime mora biti veci od 1 karaktera", category="error")
        elif password1 != password2:
            flash("Šifre se ne poklapaju", category="error")
        elif len(password1) < 7:
            flash("Šifra mora biti veci od 7 karaktera", category="error")
        else:
            novi_korisnik = User(email=email, firstName=firstName,
                                 password=generate_password_hash(password1, method='sha256'))
            db.session.add(novi_korisnik)
            db.session.commit()
            login_user(user, remember=True)
            flash("Kreirano uspješno!", category="success")
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
