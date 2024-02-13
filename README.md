# Flask Form Submission App

This is a Flask application for submitting a form with user information and resume upload to a SQLite database.

pip install -r requirements.txt
python app.py

# Usage
Access the application through your web browser by navigating to http://localhost:5000/.
Fill out the form with your information.
Upload your resume file.
Submit the form.

# Dependencies
Flask: Web framework for building the application.
Flask-SQLAlchemy: Flask extension for interacting with SQLite database.
Python 3: Programming language used for developmen

# File structures 
app.py: Contains the main Flask application.
templates/home2.html: HTML template for the homepage.
data.db: SQLite database file.
README.md: This file.

# Database Schema
Form table:
id: Integer, primary key.
first_name: String, first name of the user.
surname: String, surname of the user.
employment: String, employment information of the user.
email: String, email address of the user.
date: Date, submission date.
resume: BLOB, binary data of the uploaded resume.

# Contributing
Contributions are welcome! Please feel free to fork this repository and submit pull requests to suggest improvements or fix issues.
