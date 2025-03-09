import math


def fermat_factoring_method(n):
    a = math.isqrt(n) + 1
    b2 = a * a - n
    while not (int(math.isqrt(b2)) ** 2) == b2:
        a += 1
        b2 = a * a - n

    b = int(math.isqrt(b2))
    factor1 = a - b
    factor2 = a + b
    return factor1, factor2


result = fermat_factoring_method(n=5959)
print(result)
