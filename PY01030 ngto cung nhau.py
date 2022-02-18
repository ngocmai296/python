import math
n,k = [int(i) for i in input().split()]
j=1
for i in range(10**(k-1), 10**k-1):
    if math.gcd(i, n) == 1:
        print(str(i)+" ", end=' ')
        if j%10 == 0:
            print()
        j += 1
