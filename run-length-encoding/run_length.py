import regex

def decode(text):
    decompress = lambda match: int(match.group(0)[:-1]) * match.group(0)[-1]
    return regex.sub(r'\p{N}+.', decompress, text)

def encode(text):
    compress = lambda match: str(len(match.group(0))) + match.group(0)[0]
    return regex.sub(r'(.)\1+', compress, text)
