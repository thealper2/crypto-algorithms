def modular_exponentiation(base, exponent, mod):
    result = 1
    base = base % mod
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % mod

        exponent = exponent // 2
        base = (base * base) % mod

    return result

result = modular_exponentiation(base=5, exponent=117, mod=13)
print(result)