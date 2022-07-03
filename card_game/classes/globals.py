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

MAX_DIMENSIONS = {
    "x": 4, # rows
    "y": 5  # cols
}

STARTING_ACTIVE_SPACES = {
    "x": 2, # rows
    "y": 3  # cols
}

SHORT_ENV = {
    "grass": "-",
    "water": "w",
    "trees": "T",
    "mountains": "^",
    "desert": "d",
    "hellscape": "#",
    "snow": "*",
    "hills": "h",
    "pit": "x"
}

MAP = [40, 50]

PG_1 = [
    # grass, water, trees, mountains, desert, hellscape, snow, hills, pit
    {
        "name": "grass",
        "prob": [0.7894736842,0.05263157895,0.06578947368,0,0.01315789474,0,0.02631578947,0.05263157895,0,]},

    {
        "name": "water",
        "prob": [0.08403361345,0.8403361345,0.01120448179,0.01400560224,0.008403361345,0,0.01400560224,0.02801120448,0,]},
    {
        "name": "trees",
        "prob": [0.1346801347,0.03367003367,0.6734006734,0.01683501684,0.006734006734,0,0.03367003367,0.101010101,0,]},
    {
        "name": "mountains",
        "prob": [0,0.02564102564,0.05128205128,0.5128205128,0.1025641026,0.05128205128,0.1025641026,0.1538461538,0,]},
    {
        "name": "desert",
        "prob": [0.02590673575,0.0103626943,0.00518134715,0.207253886,0.518134715,0.0518134715,0.02590673575,0.1554404145,0,]},
    {
        "name": "hellscape",
        "prob": [0,0,0,0.35,0.25,0.3,0.01,0.08,0.01,]},
    {
        "name": "snow",
        "prob": [0.08,0.08,0.08,0.08,0.08,0.04,0.48,0.08,0,]},
    {
        "name": "hills",
        "prob": [0.06,0.06,0.08,0.16,0.06,0.004,0.056,0.52,0,]},
    {
        "name": "pit",
        "prob": [0,0,0,0.3,0.24,0.3,0.02,0.14,0,]},

]
