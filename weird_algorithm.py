# this is my solution for weird algorithm question of CSES problem set
n = int(input())
while n!=1:
    print(n,end=" ")
    if n%2 == 0:
        n = int(n/2)
    else:
        n = int(3*n+1) 
print('1')