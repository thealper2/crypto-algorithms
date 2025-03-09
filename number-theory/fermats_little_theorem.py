def format_mod_exp(a, n, p):
    n = n % (p - 1)
    result = pow(a, n, p)
    return result


result = format_mod_exp(a=3, n=6, p=7)
print(result)
