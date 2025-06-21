COLOUR_TO_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff", "Alizarin crimson": "#e32636",
           "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7",
           "Apricot": "#fbceb1", "Aqua": "#00ffff"}

for name in COLOUR_TO_CODE:
    print(f"{name:16} is {COLOUR_TO_CODE[name]}")

colour_name = input("Enter short state: ").title()
while colour_name != "":
    try:
        print(colour_name, "is", COLOUR_TO_CODE[colour_name])
    except KeyError:
        print("Invalid short state")
    colour_name = input("Enter short state: ").title()



