from functools import reduce

def largest_product(number, n):
    return max(reduce(lambda x,y: x*y, l, 1) for l in slices(number, n))

def slices(number, n):
    if len(number) < n: raise ValueError("No match possible")
    return [[int(x) for x in number[i:i+n]] for i in range(len(number) + 1 - n)]
