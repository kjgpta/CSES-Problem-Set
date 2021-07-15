def func(n,x,ar):
    for i in range(n):
        for j in range(i+1,n):
            if x == ar[i] + ar[j]:
                return str(i+1) + " " + str(j+1)
    return "IMPOSSIBLE"

    
n,x = map(int,input().split())
ar = list(map(int,input().split()))
print(func(n,x,ar))