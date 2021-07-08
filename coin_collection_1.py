import sys
sys.setrecursionlimit(10000)

def no_of_ways(target_sum,list):
    if target_sum == 0:
        return 1
    no_of_combination = 0
    for num in list:
        rem = target_sum - num
        if rem>=0:
            combination = no_of_ways(rem,list)
            if combination != 0:
                no_of_combination += combination
    return no_of_combination



no_of_items,net_sum = map(int,input().split())
list_of_numbers = list(map(int,input().split()))
print(no_of_ways(net_sum,list_of_numbers))
