def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


result = gcd(a=48, b=18)
print(result)
