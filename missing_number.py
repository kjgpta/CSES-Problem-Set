n = int(input())
l = sorted(list(map(int,input().split())),reverse=True)
j = 0
if l[-1] != 1:
    print(1)
else:
    for i in range(n,1,-1):
        if i != l[j]:
            print(i)
            break
        j += 1
