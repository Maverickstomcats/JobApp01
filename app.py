from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

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


    return render_template("index.html")

app.run(debug=True, port=5001)
