## app.py

from flask import flash,render_template,redirect,request,url_for
from flask_login import login_user,logout_user,login_required
from myproject import db,app
from myproject.models import User
from myproject.forms import RegistrationForm,Login

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/welcome")
@login_required
def welcome():
    return render_template("welcome_page.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for("home"))


@app.route("/register",methods=["GET","POST"])
def register():

    form=RegistrationForm()

    if form.validate_on_submit():

        user=User(email=form.email.data,
                              username=form.username.data,
                              hashed_password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("registration.html",form=form)

@app.route("/login",methods=["GET","POST"])
def login():

    form=Login()

    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()

        if user.check_pass(form.password.data) and user is not None:
            login_user(user)
            flash("Logged in Successfully")

            next=request.args.get("next")

            if next==None or not next[0]=='/':
                return redirect(url_for("welcome"))
            else:
                return redirect("next")

    return render_template("login.html",form=form)

