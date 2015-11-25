def slices(number, n):
    if not n or len(number) < n: raise ValueError("No match possible")
    sub = lambda number, n: [int(number[i]) for i in range(n)]
    return [sub(number[i:], n) for i in range(len(number) + 1 - n)]

