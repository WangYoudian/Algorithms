def fac(n):
	if n <= 0:
		print('Illegal input!')
	if n == 1:
		return 1
	return n * fac(n-1)

# 120
print(fac(5))