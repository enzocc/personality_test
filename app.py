import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/personality.db'

@app.route('/')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    app.run(debug=True)