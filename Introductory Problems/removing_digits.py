n = int(input())
k = []
while n != 0:
    k.append(n)
    s = list(map(int,list(str(n))))
    t = max(s)
    n -= t
print(len(k))