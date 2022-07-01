from .type import Type

TYPES = {
    "nocturnal": Type(
        name="nocturnal",
        desc="Operates best in the night.",
        logic={}
        ),
    "diurnal": Type(
        name="diurnal",
        desc="Operates best in the day.",
        logic={}
        ),
    "immobile": Type(
        name="immobile",
        desc="Cannot move.",
        logic={}
        ),
    "healer": Type(
        name="healer",
        desc="Friendly healer.",
        logic={}
        ),
    "flying": Type(
        name="flying",
        desc="Has wings!.",
        logic={}
        ),
    "cool": Type(
        name="cool",
        desc="Ay-o Daddi-o!",
        logic={}
        ),
    "offensive": Type(
        name="offensive",
        desc="Oh brother, this guy stinks!",
        logic={}
        ),
    "water": Type(
        name="water",
        desc="It is water.",
        logic={}
        ),
    "arid": Type(
        name="arid",
        desc="Embraces desolate environments.",
        logic={}
        ),
    "ice": Type(
        name="ice",
        desc="Cold.",
        logic={}
        ),
    "dragon": Type(
        name="dragon",
        desc="That of legends.",
        logic={}
        ),
    "elven": Type(
        name="elven",
        desc="Ancient humanoid race.",
        logic={}
        ),
    "demon": Type(
        name="demon",
        desc="Hailing from an evil dimension.",
        logic={}
        ),
    "tiny": Type(
        name="tiny",
        desc="Teehee! Look at the little bean.",
        logic={}
        ),
}

SKILLS = [

]

PG_1 = [
    # grass, water, trees, mountains, desert, hellscape, snow, hills, pit
    {
        "name": "grass",
        "prob": [0.5714285714, 0.1142857143, 0.1428571429, 0, 0.02857142857, 0, 0.02857142857, 0.1142857143, 0]},

    {
        "name": "water",
        "prob": [0.1910828025, 0.6369426752, 0.02547770701, 0.03184713376, 0.01910828025, 0, 0.03184713376, 0.06369426752,
               0]},
    {
        "name": "trees",
        "prob": [0.2030456853, 0.05076142132, 0.5076142132, 0.02538071066, 0.01015228426, 0, 0.05076142132, 0.152284264, 0]},
    {
        "name": "mountains",
        "prob": [0, 0.02564102564, 0.05128205128, 0.5128205128, 0.1025641026, 0.05128205128, 0.1025641026, 0.1538461538, 0]},
    {
        "name": "desert",
        "prob": [0.02590673575, 0.0103626943, 0.00518134715, 0.207253886, 0.518134715, 0.0518134715, 0.02590673575, 0.1554404145, 0]},
    {
        "name": "hellscape",
        "prob": [0, 0, 0, 0.35, 0.25, 0.3, 0.01, 0.08, 0.01]},
    {
        "name": "snow",
        "prob": [0.08, 0.08, 0.08, 0.08, 0.08, 0.04, 0.48, 0.08, 0]},
    {
        "name": "hills",
        "prob": [0.075, 0.075, 0.1, 0.2, 0.075, 0.005, 0.07, 0.4, 0]},
    {
        "name": "pit",
        "prob": [0, 0, 0, 0.3, 0.24, 0.3, 0.02, 0.14, 0]},

]
