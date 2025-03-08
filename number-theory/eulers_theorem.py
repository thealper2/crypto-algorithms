def gcd(a, b):
    while b != 0:
        a, b = b, a % b
        
    return a

def phi_function(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p

            result -= result // p

        p += 1

    if n > 1:
        result -= result // n

    return result

def euler_mod_exp(a, n):
    phi_n = phi_function(n)
    if gcd(a, n) != 1:
        raise ValueError("")

    return pow(a, phi_n, n)

result = euler_mod_exp(a=7, n=12)
print(result)