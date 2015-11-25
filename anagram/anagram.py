def detect_anagrams(original, candidates):
    return [c for c in candidates if is_anagram(original, c)]

def is_anagram(a, b):
    a = a.lower()
    b = b.lower()
    return a != b and sorted(a) == sorted(b)
