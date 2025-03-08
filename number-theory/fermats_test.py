import random

def fermat_primality_test(n, k=5):
    for _ in range(k):
        a = random.randint(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False

    return True

result = fermat_primality_test(n=11)
print(result)