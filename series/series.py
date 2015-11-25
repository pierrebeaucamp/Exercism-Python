def slices(number, n):
    sub = lambda number, n: [int(number[i]) for i in range(n)]
    out = [sub(number[i:], n) for i in range(len(number) + 1 - n)]
    if not out or not n: raise ValueError("No match possible")
    return out

