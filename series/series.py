def slices(number, n):
    if not n or len(number) < n: raise ValueError("No match possible")
    return [[int(x) for x in number[i:i+n]] for i in range(len(number) + 1 - n)]

