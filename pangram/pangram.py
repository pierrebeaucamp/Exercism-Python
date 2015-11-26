import string
import regex

def is_pangram(i):
    l = sorted(list(set(regex.sub(r'[^a-z]', "", i.lower()))))
    return l == list(string.ascii_lowercase)
