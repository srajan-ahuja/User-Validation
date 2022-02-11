import re
import db_connection

def check_string(string):

    pat = re.compile(r"^[a-zA-Z ,.’'-]+$")

    quotes = re.compile(
        r"/[’']{2}|([a-zA-z\s]?['’][a-zA-z\s]*['’][a-zA-z\s]?)|[-]{2}|([a-zA-z\s]?-[a-zA-z\s]*-[a-zA-z\s]?)|([a-zA-z]*\s[a-zA-z]*\s[a-zA-z]*\s[a-zA-z])|[\s]{2}/gm")

    if re.fullmatch(pat, string):
        if re.search(quotes, string):
            return 1
        else:
            return 0
    else:
        return 1

def check_no(phone):

    pat = re.compile(r"^\+?\d{0,3}\s?\(?\d{0,3}\)?[-.\s]?\d{0,3}[-.\s]?\d{3,4}?$")
    black = re.compile(r"\([0-9]{3}\)\s[0-9]*-[0-9]*|^[0-9]{0,3}$|[0-9]{10}")

    if re.fullmatch(pat, phone):
        if re.search(black,phone):
            return 1
        else:
            return 0
    else:
        return 1

