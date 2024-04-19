"""
Global entry to package functionality.
Will be delegating to specialized functions such as
interpolate-text, interpolate-dict, and interpolate-list.
"""
def interpolate(file, **replacements):
    with open(file, "r") as file:
        contents = file.read()
        replaced = contents.format(**replacements)
    return replaced



