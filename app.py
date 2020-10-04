import requests
import json
from scipy import stats
from flask import (
    Flask, render_template, request, redirect, url_for, flash
)
from flask_sqlalchemy import SQLAlchemy

from calculations.personality_averages import calc_points

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
        e_ans = {
            "e1": self.e1, "e2": self.e2, "e3": self.e3, "e4": self.e4,
            "e5": self.e5, "e6": self.e6, "e7": self.e7, "e8": self.e8,
            "e9": self.e9, "e10": self.e10
        }
        return calc_points(**e_ans)["extraversion"]

    @property
    def total_n(self):
        n_ans = {
            "n1": self.n1, "n2": self.n2, "n3": self.n3, "n4": self.n4,
            "n5": self.n5, "n6": self.n6, "n7": self.n7, "n8": self.n8,
            "n9": self.n9, "n10": self.n10
        }
        return calc_points(**n_ans)["neuroticism"]

    @property
    def total_a(self):
        a_ans = {
            "a1": self.a1, "a2": self.a2, "a3": self.a3, "a4": self.a4,
            "a5": self.a5, "a6": self.a6, "a7": self.a7, "a8": self.a8,
            "a9": self.a9, "a10": self.a10
        }
        return calc_points(**a_ans)["agreeableness"]

    @property
    def total_c(self):
        c_ans = {
            "c1": self.c1, "c2": self.c2, "c3": self.c3, "c4": self.c4,
            "c5": self.c5, "c6": self.c6, "c7": self.c7, "c8": self.c8,
            "c9": self.c9, "c10": self.c10
        }
        return calc_points(**c_ans)["conscientiousness"]

    @property
    def total_o(self):
        o_ans = {
            "o1": self.o1, "o2": self.o2, "o3": self.o3, "o4": self.o4,
            "o5": self.o5, "o6": self.o6, "o7": self.o7, "o8": self.o8,
            "o9": self.o9, "o10": self.o10
        }
        return calc_points(**o_ans)["openness"]

    def __repr__(self):
        return "Personanality(id={}, e={}, n={}, a={}, c={}, o={})".format(
            self.id, self.total_e, self.total_n, self.total_a,
            self.total_c, self.total_o
        )


class Personalities(object):
    def __init__(self):
        self.all_e = [p.total_e for p in Personality.query]
        self.all_n = [p.total_n for p in Personality.query]
        self.all_a = [p.total_a for p in Personality.query]
        self.all_c = [p.total_c for p in Personality.query]
        self.all_o = [p.total_o for p in Personality.query]


@app.route('/', methods=["POST"])
def index_post():
    # Get values of the radio buttons from test.html
    ans = request.values
    # Transform those values to integers
    int_ans = {k: int(ans[k]) for k in ans.keys()}
    # Calculate total points
    res = json.dumps(calc_points(**int_ans))
    # Send total points to results.html
    return redirect(url_for("results_get", results=res))


@app.route('/')
def index_get():
    return render_template("test.html")


@app.route('/results')
def results_get():
    results = json.loads(request.args['results'])
    p_o = stats.percentileofscore(ALL_PEOPLE.all_o, results["openness"])
    p_c = stats.percentileofscore(ALL_PEOPLE.all_c, results["conscientiousness"])   # noqa
    p_e = stats.percentileofscore(ALL_PEOPLE.all_e, results["extraversion"])
    p_a = stats.percentileofscore(ALL_PEOPLE.all_a, results["agreeableness"])
    p_n = stats.percentileofscore(ALL_PEOPLE.all_n, results["neuroticism"])

    percentile = {
        "openness": round(p_o, 2),
        "conscientiousness": round(p_c, 2),
        "extraversion": round(p_e, 2),
        "agreeableness": round(p_a, 2),
        "neuroticism": round(p_n, 2),
    }
    return render_template(
        "results.html", results=results, percentile=percentile
    )


if __name__ == '__main__':
    # Calculate the averages for all people
    ALL_PEOPLE = Personalities()
    app.run(debug=True)
