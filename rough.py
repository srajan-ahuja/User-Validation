import re

def check_string():

    string = input("enter input")

    pat = re.compile(r"^[a-z ,.'’-]+$")
    quotes = re.compile(r"[’']{2}|([a-zA-z\s]?['’][a-zA-z\s]*['’][a-zA-z\s]?)|[-]{2}|([a-zA-z\s]?-[a-zA-z\s]*-[a-zA-z\s]?)|([a-zA-z]*\s[a-zA-z]*\s[a-zA-z]*\s[a-zA-z])|[\s]{2}")


    if re.fullmatch(pat, string):

        if re.fullmatch(quotes, string):
            print('invalid string')
        else:
            print('Valid input')

    else:
        print('Invalid input')


check_string()