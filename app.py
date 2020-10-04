import requests
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

from calculations.personality_averages import calc_averages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/personality.db'


@app.route('/', methods=["POST"])
def index_post():
    ans = request.values
    int_ans = {k: int(ans[k]) for k in ans.keys()}
    res = calc_averages(**int_ans)
    return redirect(url_for("index_get"))


@app.route('/')
def index_get():
    return render_template("test.html")


if __name__ == '__main__':
    app.run(debug=True)
