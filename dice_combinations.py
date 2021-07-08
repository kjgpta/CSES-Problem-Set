def count(n):
	if (n == 0):
		return 1
	cnt = 0
	for i in range(1, 7):
		if (n - i >= 0):
			cnt = cnt + count(n - i)
	return cnt

if __name__ == '__main__':	
	n = int(input())
	print(count(n))