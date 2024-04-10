import os


# functions:
# - interpolate
# - interpolate-text
# - interpolate-dict
# - interpolate-list??



def read_prompt(promptfile, **replacements):
    with open(os.path.join(prompts_dir, promptfile), "r") as file:
        contents = file.read()
        replaced = contents.format(**replacements)
    return replaced



