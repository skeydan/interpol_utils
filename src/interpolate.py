# functions:
# - interpolate
# - interpolate-text
# - interpolate-dict
# - interpolate-list??



def interpolate(file, **replacements):
    with open(file, "r") as file:
        contents = file.read()
        replaced = contents.format(**replacements)
    return replaced



