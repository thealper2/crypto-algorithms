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

def is_primitive_root(g, n):
    phi_n = phi_function(n)
    residues = set()
    for k in range(1, phi_n + 1):
        residues.add(pow(g, k, n))
    return len(residues) == phi_n

def find_primitive_roots(n):
    phi_n = phi_function(n)
    primitive_roots = []
    for g in range(1, n):
        if gcd(g, n) == 1 and is_primitive_root(g, n):
            primitive_roots.append(g)
    return primitive_roots

result = find_primitive_roots(n=7)
print(result)