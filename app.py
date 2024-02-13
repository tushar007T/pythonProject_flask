from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config["SECRET_KEY"] = "tusharapplication"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    surname = db.Column(db.String(80))
    employment = db.Column(db.String(80))
    email = db.Column(db.String(80))
    date = db.Column(db.Date)
    resume = db.Column(db.BLOB)


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        first_name = request.form["name"]
        surname = request.form["surname"]
        email = request.form["email"]
        employment = request.form["employment"]
        resume = request.files["resume"]
        resume_data = resume.read()
        date = request.form["date"]
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        form = Form(first_name=first_name, surname=surname
                    ,email=email,employment=employment,resume=resume_data,
                    date=date_obj)
        db.session.add(form)
        db.session.commit()
    return render_template('home2.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5000)
