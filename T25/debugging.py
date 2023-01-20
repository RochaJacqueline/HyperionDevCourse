# Changed the index of dictionary 'k' to the variable 'key'
def print_values_of(dictionary, keys):
    for key in keys:
        print(dictionary[key])

# Changed the single quotation marks to double quotation marks around the value "d'oh" of key "homer", and added an exclamation mark after it
simpson_catch_phrases = {"lisa": "BAAAAAART!", "bart": "Eat My Shorts!", "marge": "Mmm~mmmmm", "homer": "d'oh!", "maggie": " (Pacifier Suck)"}

# Changed the type of parameters 'lisa', 'bart', 'homer' from string to a list a strings,
# since the function print_values_of expects an iterable argument keys of this type
print_values_of(simpson_catch_phrases, ['lisa', 'bart', 'homer'])

'''
    Expected console output:

    BAAAAAART!
    Eat My Shorts!
    d'oh!

'''

