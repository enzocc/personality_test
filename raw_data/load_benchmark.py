from app import db, Personality
import json

FILE_NAME = "data.json"


def load_data(data):
    res = []
    for d in data:
        if all([
            d["e1"], d["e2"], d["e3"], d["e4"], d["e5"],
            d["e6"], d["e7"], d["e8"], d["e9"], d["e10"],
            d["n1"], d["n2"], d["n3"], d["n4"], d["n5"],
            d["n6"], d["n7"], d["n8"], d["n9"], d["n10"],
            d["a1"], d["a2"], d["a3"], d["a4"], d["a5"],
            d["a6"], d["a7"], d["a8"], d["a9"], d["a10"],
            d["c1"], d["c2"], d["c3"], d["c4"], d["c5"],
            d["c6"], d["c7"], d["c8"], d["c9"], d["c10"],
            d["o1"], d["o2"], d["o3"], d["o4"], d["o5"],
            d["o6"], d["o7"], d["o8"], d["o9"], d["o10"],
        ]):
            res.append(Personality(
                race=d["race"],
                age=d["age"],
                engnat=d["engnat"],
                gender=d["gender"],
                hand=d["hand"],
                country=d.get("country", None),
                source=d["source"],
                e1=d["e1"],
                e2=d["e2"],
                e3=d["e3"],
                e4=d["e4"],
                e5=d["e5"],
                e6=d["e6"],
                e7=d["e7"],
                e8=d["e8"],
                e9=d["e9"],
                e10=d["e10"],
                n1=d["n1"],
                n2=d["n2"],
                n3=d["n3"],
                n4=d["n4"],
                n5=d["n5"],
                n6=d["n6"],
                n7=d["n7"],
                n8=d["n8"],
                n9=d["n9"],
                n10=d["n10"],
                a1=d["a1"],
                a2=d["a2"],
                a3=d["a3"],
                a4=d["a4"],
                a5=d["a5"],
                a6=d["a6"],
                a7=d["a7"],
                a8=d["a8"],
                a9=d["a9"],
                a10=d["a10"],
                c1=d["c1"],
                c2=d["c2"],
                c3=d["c3"],
                c4=d["c4"],
                c5=d["c5"],
                c6=d["c6"],
                c7=d["c7"],
                c8=d["c8"],
                c9=d["c9"],
                c10=d["c10"],
                o1=d["o1"],
                o2=d["o2"],
                o3=d["o3"],
                o4=d["o4"],
                o5=d["o5"],
                o6=d["o6"],
                o7=d["o7"],
                o8=d["o8"],
                o9=d["o9"],
                o10=d["o10"]
            ))
    db.session.add_all(res)
    db.session.commit()


if __name__ == "__main__":
    # Read data from the JSON file. Only used the first time you are trying
    # to load the benchmarks to the database
    with open(FILE_NAME, "r") as ff:
        data = json.load(ff)
    load_data(data['data'])
