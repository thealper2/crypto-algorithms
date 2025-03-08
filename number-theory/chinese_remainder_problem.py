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

def chinese_remainder_problem(a, m):
    M = 1
    for mod in m:
        M *= mod

    x = 0
    for i in range(len(m)):
        Mi = M // m[i]
        Ni = modular_inverse(Mi, m[i])
        x += a[i] * Mi * Ni

    return x % M

result = chinese_remainder_problem(a=[2,3,2], m=[3,5,7])
print(result)