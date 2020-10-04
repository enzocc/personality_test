scores = {
    "+": [1, 2, 3, 4, 5],
    "-": [5, 4, 3, 2, 1]
}
e_questions = {
    "q1": "+", "q6": "-", "q11": "+", "q16": "-", "q21": "+",
    "q26": "-", "q31": "+", "q36": "-", "q41": "+", "q46": "-"
}
a_questions = {
    "q2": "-", "q7": "+", "q12": "-", "q17": "+", "q22": "-",
    "q27": "+", "q32": "-", "q37": "+", "q42": "+", "q47": "+"
}
c_questions = {
    "q3": "+", "q8": "-", "q13": "+", "q18": "-", "q23": "+",
    "q28": "-", "q33": "+", "q38": "-", "q43": "+", "q48": "+"
}
n_questions = {
    "q4": "-", "q9": "+", "q14": "-", "q19": "+", "q24": "-",
    "q29": "-", "q34": "-", "q39": "-", "q44": "-", "q49": "-"
}
o_questions = {
    "q5": "+", "q10": "-", "q15": "+", "q20": "-", "q25": "+",
    "q30": "-", "q35": "+", "q40": "+", "q45": "+", "q50": "+"
}


def openness(**kwargs):
    return [scores[o_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def conscientiousness(**kwargs):
    return [scores[c_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def extroversion(**kwargs):
    return [scores[e_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def agreeableness(**kwargs):
    return [scores[a_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def neuroticism(**kwargs):
    return [scores[n_questions[k]][kwargs[k]-1] for k in kwargs.keys()]


def calc_averages(**kwargs):
    # openness
    dict_oo = {k: kwargs[k] for k in kwargs.keys() if k in o_questions}
    o_result = sum(openness(**dict_oo))
    # conscientiousness
    dict_cc = {k: kwargs[k] for k in kwargs.keys() if k in c_questions}
    c_result = sum(conscientiousness(**dict_cc))
    # extroversion
    dict_ee = {k: kwargs[k] for k in kwargs.keys() if k in e_questions}
    e_result = sum(extroversion(**dict_ee))
    # agreeableness
    dict_aa = {k: kwargs[k] for k in kwargs.keys() if k in a_questions}
    a_result = sum(agreeableness(**dict_aa))
    # neuroticism
    dict_nn = {k: kwargs[k] for k in kwargs.keys() if k in n_questions}
    n_result = sum(neuroticism(**dict_nn))

    return {
        "openness": o_result,
        "conscientiousness": c_result,
        "extroversion": e_result,
        "agreeableness": a_result,
        "neuroticism": n_result,
    }
