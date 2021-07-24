def func(n):
    s=sum(range(n+1))
    if n==0 or s%2!=0:
        return 0
    else:
        s = s//2
        dp = [[0 for i in range(s+1)] for j in range(n+1)]
        dp[0][0]=1
        for i in range(1,n+1):
            for j in range(1,s+1):
                if i<=j:
                    dp[i][j]=dp[i-1][j-i]+dp[i-1][j]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[n][s]%1000000007
n = int(input())
result = func(n)
print(result) 