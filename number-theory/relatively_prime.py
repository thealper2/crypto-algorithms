def relatively_prime(a, b):
    while b != 0:
        a, b = b, a % b

    return a == 1


result = relatively_prime(a=35, b=64)
print(result)
