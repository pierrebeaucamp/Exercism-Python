def square_of_sum(x):
    return (x * (x + 1) / 2) ** 2

def sum_of_squares(x):
    return sum(i ** 2 for i in range(x + 1))

def difference(x):
    return square_of_sum(x) - sum_of_squares(x)
