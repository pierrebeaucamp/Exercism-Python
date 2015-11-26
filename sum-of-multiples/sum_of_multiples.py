def sum_of_multiples(n, lst=[3, 5]):
    return sum(set(i for l in lst for i in range(n) if l and i % l == 0))
