n=int(input())
if(n==0 or n==1):
    print("Not Prime")
    exit()
    
is_prime=False
for i in range(2, n):
    if(n%i==0):
        print("Not Prime")
        is_prime=True
        break

if(is_prime==False):
    print("Prime") 