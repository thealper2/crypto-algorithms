def extended_gcd(a, n):
    if n == 0:
        return a, 1, 0

    gcd_, x1, y1 = extended_gcd(n, a % n)
    x = y1
    y = x1 - (a // n) * y1
    return gcd_, x, y


result = extended_gcd(a=30, n=50)
print(result)
