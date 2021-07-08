# we have imported sys library to modify the recursion limit to 10000 
import sys
sys.setrecursionlimit(10000)

def best_sum(target_sum, numbers):
    memo = {}
    def helper(target_sum, numbers):
        if target_sum == 0:
            return []
        if target_sum in memo:
            return memo[target_sum]
        shortest_combination = None
        for num in numbers:
            remainder = target_sum - num
            if remainder >= 0:
                combination = helper(remainder, numbers)
                if combination is not None:
                    combination = combination + [num]
                    if shortest_combination is None or len(combination) < len(shortest_combination):
                        shortest_combination = combination
        memo[target_sum] = shortest_combination
        return memo[target_sum]
    return helper(target_sum, numbers)


no_of_items,net_sum = map(int,input().split())
list_of_numbers = list(map(int,input().split()))
print(len(best_sum(net_sum,list_of_numbers)))


