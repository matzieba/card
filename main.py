from flask import Flask, render_template, redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email
import os
from flask_bootstrap import Bootstrap
import smtplib



app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
bootstrap = Bootstrap(app)



class ContactForm(FlaskForm):
    title = StringField("Message topic", validators=[DataRequired()])
    email = StringField("Your email", validators=[DataRequired(), Email()])
    body = StringField("Your message", validators=[DataRequired()])
    submit = SubmitField("Send")

SECRET_KEY = "76736jfmsdkgsadmk53953uasfa@#$%%"

@app.route("/")
def main():
    is_main = True
    return render_template('index.html', is_main=is_main)

@app.route("/manager")
def manager():
    is_main = False
    return render_template('manager.html', is_main=is_main)

@app.route("/developer")
def developer():
    is_main = False
    return render_template('developer.html', is_main=is_main)

@app.route("/dog")
def dog():
    is_main = False
    return render_template('dog.html', is_main=is_main)

@app.route("/climber")
def climber():
    is_main = False
    return render_template('climber.html', is_main=is_main)

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        message = {
            "title":form.title.data,
            "email":form.email.data,
            "message":form.body.data,
        }
        my_email = os.environ.get("my_email")
        password = os.environ.get("password")
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="matizieba@gmail.com",
                                msg=message['message'],)
            return redirect(url_for('main'))
    is_main = False
    return render_template('contact.html', form=form)


if __name__ == "__main__":
    app.run()

