scores = {
    "+": [1, 2, 3, 4, 5],
    "-": [5, 4, 3, 2, 1]
}
e_questions = {
    "e1": "+", "e2": "-", "e3": "+", "e4": "-", "e5": "+",
    "e6": "-", "e7": "+", "e8": "-", "e9": "+", "e10": "-"
}
a_questions = {
    "a1": "-", "a2": "+", "a3": "-", "a4": "+", "a5": "-",
    "a6": "+", "a7": "-", "a8": "+", "a9": "+", "a10": "+"
}
c_questions = {
    "c1": "+", "c2": "-", "c3": "+", "c4": "-", "c5": "+",
    "c6": "-", "c7": "+", "c8": "-", "c9": "+", "c10": "+"
}
n_questions = {
    "n1": "-", "n2": "+", "n3": "-", "n4": "+", "n5": "-",
    "n6": "-", "n7": "-", "n8": "-", "n9": "-", "n10": "-"
}
o_questions = {
    "o1": "+", "o2": "-", "o3": "+", "o4": "-", "o5": "+",
    "o6": "-", "o7": "+", "o8": "+", "o9": "+", "o10": "+"
}


def openness(**kwargs):
    return [scores[o_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def conscientiousness(**kwargs):
    return [scores[c_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def extraversion(**kwargs):
    return [scores[e_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def agreeableness(**kwargs):
    return [scores[a_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def neuroticism(**kwargs):
    return [scores[n_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def calc_points(**kwargs):
    # openness
    dict_oo = {k: kwargs[k] for k in kwargs.keys() if k in o_questions}
    o_result = sum(openness(**dict_oo))
    # conscientiousness
    dict_cc = {k: kwargs[k] for k in kwargs.keys() if k in c_questions}
    c_result = sum(conscientiousness(**dict_cc))
    # extraversion
    dict_ee = {k: kwargs[k] for k in kwargs.keys() if k in e_questions}
    e_result = sum(extraversion(**dict_ee))
    # agreeableness
    dict_aa = {k: kwargs[k] for k in kwargs.keys() if k in a_questions}
    a_result = sum(agreeableness(**dict_aa))
    # neuroticism
    dict_nn = {k: kwargs[k] for k in kwargs.keys() if k in n_questions}
    n_result = sum(neuroticism(**dict_nn))

    return {
        "openness": o_result,
        "conscientiousness": c_result,
        "extraversion": e_result,
        "agreeableness": a_result,
        "neuroticism": n_result,
    }
