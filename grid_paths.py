import sys
sys.setrecursionlimit(10000)

def func(grid,x,y):
    n = len(grid)
    if grid[x][y] == '*':
        return 0
    elif x == n-1 and y == n-1:
        return 1
    if x == n-1 and y != n-1:
        return func(grid,x,y+1)
    elif x != n-1 and y == n-1:
        return func(grid,x+1,y)
    return func(grid,x+1,y) + func(grid,x,y+1)


size_of_grid = int(input())
grid = []
for i in range(size_of_grid):
    grid.append(input())
x = 0
y = 0
no_of_ways = func(grid,x,y)
print(no_of_ways)