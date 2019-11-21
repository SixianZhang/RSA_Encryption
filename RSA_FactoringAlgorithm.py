import math
import time
import sys
import os


def factoring_algorithm(n, e):
    flag = True
    while flag:
        if math.gcd(n, e) != 1:
            print("e must be co-prime to N")
            continue
        if n > e > 1:
            for r in range(1, n):
                while n > 1:
                    break
                if pow(e, r, n) == 1:
                    while n > 1:
                        break
                    break
            if r % 2 == 0 and pow(e, r // 2, n) != n - 1:
                p = math.gcd(e ** (r // 2) - 1, n)
                q = math.gcd(e ** (r // 2) + 1, n)
                flag = False
            else:
                print("Error")
    print("p: ", p)
    print("q: ", q)


sample_time = []
t_all = time.time()

for b in range(5, 6):

    t_start = time.time()
    factoring_algorithm(143, 12)
    sample_time.append(time.time() - t_start)

    sys.stdout = sys.__stdout__

print((time.time() - t_all))
