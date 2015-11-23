import regex

def word_count(text):
    count = {}
    for word in regex.findall(r'[\p{L}\p{N}]+', text.lower()):
        count[word] = count.get(word, 0) + 1
    return count
