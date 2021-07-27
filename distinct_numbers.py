#this is my solution for Distinct Numbers problem in CSES dataset
no_of_integers = int(input())
array = list(map(int,input().split()))
print(len(set(array)))