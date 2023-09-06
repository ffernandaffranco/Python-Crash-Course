glossary = {
    'variable': 'variables are used to store values',
    'string': 'series of characters, surrounded by single or double quotes',
    'list': 'stores a series of items in particular order',
    'if': 'used to test for particular conditions and respond appropiately',
    'while': 'repeats a block of code as long as certain condition is true'
}

for key, value in glossary.items():
    print(f"{key.title()}: {value.capitalize()}.\n")