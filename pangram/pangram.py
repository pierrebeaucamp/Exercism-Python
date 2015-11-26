import string
import regex

def is_pangram(i):
    l = sorted(list(set(regex.sub(r'[^a-z0-9]', "", i.lower()))))
    return l == list(string.ascii_lowercase)
