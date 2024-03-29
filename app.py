from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "myapplication123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"

class Form(db.model):
    id = db.Column(db.Integer,primary_key=True)
    first_name= db.column(db.String(80))
    last_name= db.column(db.String(80))
    email= db.column(db.String(80))
    date= db.column(db.Date)
    occupation = db.Column(db.String(80))


@app.route("/",methods=["GET","POST"])

def index():
    if request.method == "POST":
        first_name = request.form["first_name"]
        last_name = request.form["last_name"]
        email = request.form["email"]
        date = request.form['date']
        occupation = request.form["occupation"]
        print("first_name")


        form = Form(first_name=first_name, last_name=last_name, email=email, date=date, occupation=occupation)
        db.session.add(form)
        db.session.commit()

    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
