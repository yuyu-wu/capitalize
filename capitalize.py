# capitalize
# Write a function called capitalize. This function accepts a string and returns the same string with the first letter capitalized.  You may want to use slices to help you out.

# capitalize("jamaica") # "Jamaica"
# capitalize("chicken") # "Chicken"

def capitalize(string):
    return f'{string[:1].upper()}{string[1:]}'
    # return string[:1].upper() + string[1:]