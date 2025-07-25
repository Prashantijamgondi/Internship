n=6
i=0
if(n==1):
    print('0')
else:
    j=1
    while n!=0:
        print(i)
        i,j=j, j+i
        n-=1
    