from .type import Type
from .utils import make_probs

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
    "pit": "x",
    "enchanted": "e",
    "clouds": "e",
}

MAP = [28, 40]

BITS = 32
BIG_BITS = BITS * 4

class Screen():
    WIDTH = MAP[1] * BITS
    HEIGHT = MAP[0] * BITS

ELEVATIONS = {
    "grass": [0,1],
    "water": [0],
    "hills": [1],
    "trees": [0,1],
    "mountains": [1,2],
    "hellscape": [0],
    "snow": [0,1],
    "pit": [0],
    "enchanted": [0,1,2,3],
    "clouds": [3],
    "desert": [0],
}

NATURAL_RAMP = ["hills", "enchanted"]

PG_1 = [
    # grass, water, trees, mountains, desert, hellscape, snow, hills, pit, enchanted, clouds
    {
        "name": "grass",
        "prob": make_probs([300, 20, 25, 0, 5, 0, 10, 20, 0, 1, 20]),
    },
    {
        "name": "water",
        "prob": make_probs([30, 300, 4, 5, 3, 0, 5, 10, 0, 5, 10]),
    },
    {
        "name": "trees",
        "prob": make_probs([40, 10, 200, 5, 2, 0, 10, 30, 0, 1, 10]),
    },
    {
        "name": "mountains",
        "prob": make_probs([0, 5, 10, 100, 20, 10, 20, 30, 0, 5, 20]),
    },
    {
        "name": "desert",
        "prob": make_probs([5, 2, 1, 40, 150, 10, 5, 30, 0, 3, 0]),
    },
    {
        "name": "hellscape",
        "prob": make_probs([0, 0, 0, 35, 25, 30, 1, 8, 1, 10, 0]),
    },
    {
        "name": "snow",
        "prob": make_probs([10, 10, 10, 10, 10, 5, 100, 10, 0, 1, 10]),
    },
    {
        "name": "hills",
        "prob": make_probs([15, 15, 20, 40, 15, 1, 14, 130, 0, 1, 10]),
    },
    {
        "name": "pit",
        "prob": make_probs([0, 0, 0, 15, 12, 15, 1, 7, 0, 50, 10]),
    },
    {
        "name": "enchanted",
        "prob": make_probs([3, 3, 10, 10, 5, 25, 5, 3, 0, 2, 25]),
    },
    {
        "name": "clouds",
        "prob": make_probs([20, 10, 15, 20, 0, 0, 10, 10, 1, 1, 30]),
    },
    # grass, water, trees, mountains, desert, hellscape, snow, hills, pit, enchanted, clouds

]
