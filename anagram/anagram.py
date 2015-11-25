def detect_anagrams(original, candidates):
    out = []
    for c in candidates:
        if c.lower() == original.lower(): continue
        if sorted(original.lower()) == sorted(c.lower()): out.extend([c])
    return out
