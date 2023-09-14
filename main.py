from flask import Flask, render_template, request
from flask import session, make_response, url_for
from flask import redirect, flash
from markupsafe import escape
from models import db, User
from datetime import datetime
from sqlalchemy import exc
from flask_wtf.csrf import CSRFProtect
from flask_security import Security
from flask_security.utils import encrypt_password
from forms import Register_Form, Log_in_Form

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = '03be17dc58ef996923714304a7bb296be26e4879baa8b1fc77f2dac2c7ca7523'
if 'SECURITY_PASSWORD_SALT' not in app.config:
    app.config['SECURITY_PASSWORD_SALT'] = app.config['SECRET_KEY']
app.secret_key = '03be17dc58ef996923714304a7bb296be26e4879baa8b1fc77f2dac2c7ca7523'
csrf = CSRFProtect(app)
db.init_app(app)
security = Security(app, db)


@app.route('/')
def login():
    form = Register_Form()
    return render_template('login.html', form=form)


@app.cli.command("init-db")
def init_db():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def logged():
    if 'delete' in request.form:
        session.pop('username', None)
        return redirect(url_for('login'))
    else:
        form = Register_Form()
        firstname = form.firstname.data
        secondname = form.secondname.data
        username = form.username.data
        usermail = form.usermail.data
        userpassword = form.userpassword.data

        user = User(ufname=firstname, usname=secondname, username=username, eusermail=usermail, upassword=encrypt_password(userpassword))
        try:
            db.session.add(user)
            db.session.commit()
        
            response = make_response("Logged in")
            response.set_cookie('username', username)
            response.set_cookie('usermail', usermail)
            time: str =  f"{datetime.now()}"
            form = Log_in_Form(username=username, upassword=userpassword)
            return render_template('login.html', uname=username, time=time, form=form)
        except exc.IntegrityError:
            flash("User already exist.", "error")
            return render_template('login.html', form=form)


if __name__ == "__main__":
    app.run(debug=True)
