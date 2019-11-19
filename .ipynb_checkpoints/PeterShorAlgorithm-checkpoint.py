import math
# Knowing N and picking a, lets find P and Q to break RSA.
print("Lets break RSA using Shor's Algorithm.")
N = int(input("Enter a value N to determine PxQ: "))
Flag = True
while Flag:
    a = int(input("Enter a value a between 0 and N: "))
    if math.gcd(N, a) != 1:
        print("a and N must be co-prime.")
        print("or, a must be less than N and greater than 0.")
        continue
    if N > a > 1:
        for r in range(1, N):           # Find r
            while N > 1:
                print(r)
                break
            if pow(a, r, N) == 1:       # f(r) -> a^r congruent 1 mod N, return x to the power y, modulo z
                while N > 1:
                    print("f(r) =", pow(a, r, N))
                    break
                break
        print("a = ", a)
        print("r =", r)
        if r % 2 == 0 and pow(a, r // 2, N) != N - 1:
            p = math.gcd(a ** (r // 2) - 1, N)
            q = math.gcd(a ** (r // 2) + 1, N)
            Flag = False
        else:
            print("Error: Enter a new a")  # Cannot be N and 1
print("The value for P is %d, The value for Q is %d" % (p, q))
print("N =", p*q)
