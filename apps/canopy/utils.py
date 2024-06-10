import random

adjectives = [
    "Magnificent",
    "Exquisite",
    "Radiant",
    "Splendid",
    "Majestic",
    "Elegant",
    "Sublime",
    "Resplendent",
    "Impeccable",
    "Opulent",
    "Grandiose",
    "Stupendous",
    "Glorious",
    "Enchanting",
    "Effervescent",
    "Brilliant",
    "Luminous",
    "Dazzling",
    "Vibrant",
    "Stellar",
    "Sparkling",
    "Glistening",
    "Shimmering",
    "Lustrous",
    "Fabulous",
    "Marvelous",
    "Stunning",
    "Radiant",
    "Glowing",
    "Awe-inspiring",
]

trees = [
    "Maple",
    "Birch",
    "Oak",
    "Elm",
    "Ash",
    "Pine",
    "Cedar",
    "Fir",
    "Beech",
    "Palm",
    "Spruce",
    "Larch",
    "Alder",
    "Willow",
    "Ebony",
    "Yew",
    "Holly",
    "Fig",
    "Rowan",
    "Teak",
    "Lime",
    "Cork",
    "Mango",
    "Apple",
    "Pear",
    "Plum",
    "Cherry",
    "Peach",
    "Palm",
]


def generate_unique_name():
    adjective = random.choice(adjectives)
    noun = random.choice(trees)
    number = random.randint(100, 999)
    return f"{adjective} {noun} {number}"
