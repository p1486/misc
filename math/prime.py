import math

def primes(limit):
    p = [2, 3]
    r = range(1, math.isqrt(limit) + 1)
    sieve = [False] * (limit + 1)
    for x in r:
        for y in r:
            xx = x * x
            yy = y * y
            xx3 = 3 * xx
            xx3yy = xx3 + yy            
            n = xx3yy + xx
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]
            n = xx3yy
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]
            n = xx3 - yy
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]
    for x in range(5,int(math.sqrt(limit))):
        if sieve[x]:
            xx=x*x
            for y in range(xx,limit+1,xx):
                sieve[y] = False
    for q in range(5,limit):
        if sieve[q] : p.append(q)
    return p


def miller_rabin_base_2(n):
    d, s = n - 1, 0
    while not d & 1:
        d, s = d >> 1, s + 1
    x = pow(2, d, n)
    if (x == 1) or (x == n - 1):
        return True
    for _ in range(s - 1):
        x = pow(x, 2, n)
        if x == 1:
            return False
        elif x == n - 1:
            return True
    return False


def U_V_subscript(k, n, U, V, P, Q, D):
    digits = bin(k)[3:]
    subscript = 1
    for digit in digits:
        U, V = (U * V) % n, (pow(V, 2, n) - 2 * pow(Q, subscript, n)) % n
        subscript *= 2
        if digit == '1':
            if not (P * U + V) & 1:
                if not (D * U + P * V) & 1:
                    U, V = (P * U + V) >> 1, (D * U + P * V) >> 1
                else:
                    U, V = (P * U + V) >> 1, (D * U + P * V + n) >> 1
            elif not (D * U + P * V) & 1:
                U, V = (P * U + V + n) >> 1, (D * U + P * V) >> 1
            else:
                U, V = (P * U + V + n) >> 1, (D * U + P * V + n) >> 1
            subscript += 1
            U, V = U % n, V % n
    return U, V


def lucas_pp(n, D, P, Q):
    U, V = U_V_subscript(n + 1, n, 1, P, P, Q, D)
    if U != 0:
        return False
    d = n + 1
    s = 0
    while not d & 1:
        d = d >> 1
        s += 1
    U, V = U_V_subscript(n + 1, n, 1, P, P, Q, D)
    if (U == 0) or (V == 0):
        return True
    for r in range(s - 1):
        U, V = (U * V) % n, (pow(V, 2, n) - 2 * pow(Q, d * (2**r), n)) % n
        if V == 0:
            return True
    return False


def jacobi_symbol(a, n):
    if n == 1:
        return 1
    elif a == 0:
        return 0
    elif a == 1:
        return 1
    elif a == 2:
        if n & 7 in [3, 5]:
            return -1
        elif n & 7 in [1, 7]:
            return 1
    elif a < 0:
        return (-1)**((n - 1) // 2) * jacobi_symbol(-1 * a, n)
    if not a & 1:
        return jacobi_symbol(2, n) * jacobi_symbol(a // 2, n)
    elif a % n != a:
        return jacobi_symbol(a % n, n)
    else:
        if a & 3 == n & 3 == 3:
            return -1 * jacobi_symbol(n, a)
        else:
            return jacobi_symbol(n, a)


def D_chooser(candidate):
    D = 5
    while jacobi_symbol(D, candidate) != -1:
        D += 2 if D > 0 else -2
        D *= -1
    return D


def baillie_psw(candidate):
    for known_prime in [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
    ]:
        if candidate == known_prime:
            return True
        elif candidate % known_prime == 0:
            return False
    if not miller_rabin_base_2(candidate):
        return False
    if int(candidate**0.5 + 0.5)**2 == candidate:
        return False
    D = D_chooser(candidate)
    if not lucas_pp(candidate, D, 1, (1 - D) // 4):
        return False
    return True


if __name__ == "__main__":
    p = primes(int(input(">> ")))
    print(p)
    print(len(p))
    for i in p:
        if not baillie_psw(i):
            print(False)
            break
