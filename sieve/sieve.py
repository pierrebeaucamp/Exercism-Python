def find_primes(array):
    if not array: return array
    return [array[0]] + find_primes([i for i in array if i % array[0]])

def sieve(n):
    return find_primes(list(range(2, n + 1)))

