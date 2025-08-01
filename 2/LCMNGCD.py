import math
m=int(input())
n=int(input())
print(math.gcd(m, n))
print(math.lcm(m, n))

# LCM 
max_num = max(m, n)
while True:
    if max_num % m == 0 and max_num % n == 0:
        print(max_num)
        break
    max_num += 1
    
# GCD
min_num = min(m, n)
while n:
    m,n=n, m%n
print(m)
