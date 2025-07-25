n=input()
lenght=len(n)
sums=0
for i in range(lenght):
    sums+=int(n[i])**lenght
if(sums==int(n)):
    print(True)
else:
    print(False)