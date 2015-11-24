def distance(a, b):
    count = 0
    for i, c in enumerate(a):
        if c != b[i]: count += 1
    return count
