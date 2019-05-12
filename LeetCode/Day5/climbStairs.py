def climbStairs(n):
	if n <= 2:
		return n
	return climbStairs(n-1)+climbStairs(n-2)

n = 4
print(climbStairs(n))