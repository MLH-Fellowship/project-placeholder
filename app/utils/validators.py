import re


def is_valid_email(email):
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if (re.search(regex, email)):
        return True
    else:
        return False
