import regex

def word_count(text):
    count = {}
    for word in regex.findall(r'[\p{L}\p{N}]+', text.lower()):
        count[word] = count[word] + 1 if word in count else 1
    return count
