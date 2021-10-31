from flask import render_template, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
        ):
            login_user(attempted_user)
            return redirect(url_for("dashboard"))
        else:
            flash(
                f"Incorrect Username Or Password! Please Try Again.", category="danger"
            )
            return redirect(request.url)
    return render_template("login.html", form=form)