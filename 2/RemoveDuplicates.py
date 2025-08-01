lst=list(map(int, input().split()))

for i in range(len(lst)):
    if i in lst[i:]:
        lst.remove(lst[i])
print(lst)