import regex
import string

abc = list(string.ascii_lowercase)

def decode(txt):
    txt = regex.sub(r'\p{P}+|\s', "", txt)
    return regex.sub(r'[a-z]', lambda m: abc[-abc.index(m.group(0)) -1], txt)

def encode(txt):
    return regex.sub(r'(.{5})(?!$)', '\\1 ', decode(txt.lower()))
