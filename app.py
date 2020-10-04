import requests
import json
from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from flask_sqlalchemy import SQLAlchemy

from calculations.personality_averages import calc_averages

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/personality.db'

db = SQLAlchemy(app)
ALL_PEOPLE = None


class Personality(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.Integer)
    age = db.Column(db.Integer)
    engnat = db.Column(db.Integer)
    gender = db.Column(db.Integer)
    hand = db.Column(db.Integer)
    country = db.Column(db.String(2))
    source = db.Column(db.String(50), nullable=False)
    e1 = db.Column(db.Integer, nullable=False)
    e2 = db.Column(db.Integer, nullable=False)
    e3 = db.Column(db.Integer, nullable=False)
    e4 = db.Column(db.Integer, nullable=False)
    e5 = db.Column(db.Integer, nullable=False)
    e6 = db.Column(db.Integer, nullable=False)
    e7 = db.Column(db.Integer, nullable=False)
    e8 = db.Column(db.Integer, nullable=False)
    e9 = db.Column(db.Integer, nullable=False)
    e10 = db.Column(db.Integer, nullable=False)
    n1 = db.Column(db.Integer, nullable=False)
    n2 = db.Column(db.Integer, nullable=False)
    n3 = db.Column(db.Integer, nullable=False)
    n4 = db.Column(db.Integer, nullable=False)
    n5 = db.Column(db.Integer, nullable=False)
    n6 = db.Column(db.Integer, nullable=False)
    n7 = db.Column(db.Integer, nullable=False)
    n8 = db.Column(db.Integer, nullable=False)
    n9 = db.Column(db.Integer, nullable=False)
    n10 = db.Column(db.Integer, nullable=False)
    a1 = db.Column(db.Integer, nullable=False)
    a2 = db.Column(db.Integer, nullable=False)
    a3 = db.Column(db.Integer, nullable=False)
    a4 = db.Column(db.Integer, nullable=False)
    a5 = db.Column(db.Integer, nullable=False)
    a6 = db.Column(db.Integer, nullable=False)
    a7 = db.Column(db.Integer, nullable=False)
    a8 = db.Column(db.Integer, nullable=False)
    a9 = db.Column(db.Integer, nullable=False)
    a10 = db.Column(db.Integer, nullable=False)
    c1 = db.Column(db.Integer, nullable=False)
    c2 = db.Column(db.Integer, nullable=False)
    c3 = db.Column(db.Integer, nullable=False)
    c4 = db.Column(db.Integer, nullable=False)
    c5 = db.Column(db.Integer, nullable=False)
    c6 = db.Column(db.Integer, nullable=False)
    c7 = db.Column(db.Integer, nullable=False)
    c8 = db.Column(db.Integer, nullable=False)
    c9 = db.Column(db.Integer, nullable=False)
    c10 = db.Column(db.Integer, nullable=False)
    o1 = db.Column(db.Integer, nullable=False)
    o2 = db.Column(db.Integer, nullable=False)
    o3 = db.Column(db.Integer, nullable=False)
    o4 = db.Column(db.Integer, nullable=False)
    o5 = db.Column(db.Integer, nullable=False)
    o6 = db.Column(db.Integer, nullable=False)
    o7 = db.Column(db.Integer, nullable=False)
    o8 = db.Column(db.Integer, nullable=False)
    o9 = db.Column(db.Integer, nullable=False)
    o10 = db.Column(db.Integer, nullable=False)

    @property
    def total_e(self):
        return (
            self.e1 + self.e2 + self.e3 + self.e4 + self.e5 +
            self.e6 + self.e7 + self.e8 + self.e9 + self.e10
        )

    @property
    def total_n(self):
        return (
            self.n1 + self.n2 + self.n3 + self.n4 + self.n5 +
            self.n6 + self.n7 + self.n8 + self.n9 + self.n10
        )

    @property
    def total_a(self):
        return (
            self.a1 + self.a2 + self.a3 + self.a4 + self.a5 +
            self.a6 + self.a7 + self.a8 + self.a9 + self.a10
        )

    @property
    def total_c(self):
        return (
            self.c1 + self.c2 + self.c3 + self.c4 + self.c5 +
            self.c6 + self.c7 + self.c8 + self.c9 + self.c10
        )

    @property
    def total_o(self):
        return (
            self.o1 + self.o2 + self.o3 + self.o4 + self.o5 +
            self.o6 + self.o7 + self.o8 + self.o9 + self.o10
        )

    def __repr__(self):
        return "Personanality(id={}, e={}, n={}, a={}, c={}, o={})".format(
            self.id, self.total_e, self.total_n, self.total_a,
            self.total_c, self.total_o
        )


class Personalities(object):
    def __init__(self):
        all_e = [p.total_e for p in Personality.query]
        all_n = [p.total_n for p in Personality.query]
        all_a = [p.total_a for p in Personality.query]
        all_c = [p.total_c for p in Personality.query]
        all_o = [p.total_o for p in Personality.query]

        self.avr_e = sum(all_e)/len(all_e)
        self.avr_n = sum(all_n)/len(all_n)
        self.avr_a = sum(all_a)/len(all_a)
        self.avr_c = sum(all_c)/len(all_c)
        self.avr_o = sum(all_o)/len(all_o)


@app.route('/', methods=["POST"])
def index_post():
    ans = request.values
    int_ans = {k: int(ans[k]) for k in ans.keys()}
    res = json.dumps(calc_averages(**int_ans))
    return redirect(url_for("results_get", results=res))


@app.route('/')
def index_get():
    return render_template("test.html")


@app.route('/results')
def results_get():
    results = json.loads(request.args['results'])
    all_scores = {
        "openness": round(ALL_PEOPLE.avr_o, 2),
        "conscientiousness": round(ALL_PEOPLE.avr_c, 2),
        "extroversion": round(ALL_PEOPLE.avr_e, 2),
        "agreeableness": round(ALL_PEOPLE.avr_a, 2),
        "neuroticism": round(ALL_PEOPLE.avr_n, 2),
    }
    return render_template(
        "results.html", results=results, all_people=all_scores
    )


if __name__ == '__main__':
    # Calculate the averages for all people
    ALL_PEOPLE = Personalities()
    app.run(debug=True)
