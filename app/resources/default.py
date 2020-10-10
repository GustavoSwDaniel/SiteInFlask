# pylint: disable=maybe-no-member
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.app import app, db, login_manager
from app.models.forms import LoginForm
from app.models.tables import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(user_id=user_id).first()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Logged in.")
            return redirect(url_for("index"))
        else:
            flash("Invalid login")
    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Logged out.")
    return redirect(url_for("index"))


"""
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(somewhere)"""

"""@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):"""
# create
"""i = User("Gustavo", "1234", "Gustavo Daniel", "gdaniel@gmail.com")
    db.session.add(i)
    db.session.commit()
    return "Ok"""

# read
"""r = User.query.filter_by(username="GustavoDaniel").all()
    print(r)
    return "ok"""

# upgrade
"""u = User.query.filter_by(username="GustavoDaniel").first()
    r.name = "Gustavo D."
    db.session.add(r)
    db.session.commit()
    return "ok"""

# delete
"""d = User.query.filter_by(username="GustavoDaniel").first()
    db.session.delete(r)
    db.session.commit()
    return "ok"""