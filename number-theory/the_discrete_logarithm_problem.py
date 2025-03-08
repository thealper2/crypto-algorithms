def discrete_logarithm_problem(base, result, modulus):
    for x in range(modulus):
        if pow(base, x, modulus) == result:
            return x

    return None

result = discrete_logarithm_problem(base=2, result=11, modulus=19)
print(result)