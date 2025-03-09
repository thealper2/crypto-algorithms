def extended_gcd(a, n):
    if n == 0:
        return a, 1, 0

    gcd_, x1, y1 = extended_gcd(n, a % n)
    x = y1
    y = x1 - (a // n) * y1
    return gcd_, x, y


def modular_inverse(a, n):
    gcd_, x, _ = extended_gcd(a, n)
    if gcd_ != 1:
        raise ValueError("")

    return x % n


result = modular_inverse(a=3, n=7)
print(result)
