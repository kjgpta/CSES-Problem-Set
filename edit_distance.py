def func(a, b, m, n):
    if m == 0:
	    return n
    if n == 0:
	    return m
    if a[m-1] == b[n-1]:
	    return func(a, b, m-1, n-1)
	
    return 1 + min(func(a, b, m, n-1), func(a, b, m-1, n), func(a, b, m-1, n-1))

a = input()
b = input()
print(func(a, b, len(a), len(b)))
