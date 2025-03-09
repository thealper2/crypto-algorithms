def modular_arithmetic(a, b, mod, base, exponent):
    multiply_result = a * b
    mod_multiply = multiply_result % mod
    power_result = base**exponent
    mod_power = power_result % mod
    total = mod_multiply + mod_power
    result = total % mod
    return result


result = modular_arithmetic(a=17, b=13, mod=7, base=5, exponent=3)
print(result)
