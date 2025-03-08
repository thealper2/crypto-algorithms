import random

def miller_rabin_test(n, k=5):
    if n <= 1 or n == 4:
        return False
    
    if n <= 3:
        return True
    
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        
        else:
          return False
            
    return True

result = miller_rabin_test(n=13)
print(result)