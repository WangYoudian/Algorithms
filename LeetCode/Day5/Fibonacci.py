# 使用生成器返回斐波那契数列的第k项
class Fibonacci:
	def __init__(self):
		self.aList = [0, 1]

	def generate(self):
		if n<=1:
			return self.aList[n]
		self.aList.append(self.aList[-1]+self.aList[-2])
		return self.aList[-1]
# 1,1,2,3,5
f = Fibonacci()
n = 10
for i in range(10):
	fib_num = f.generate()
print(fib_num)
print(f.aList)

def fib(n):
	nums = [0, 1]
	while n >= 1:
		nums.append(nums[-1]+nums[-2])
		n -= 1
		
	print(nums)
	return nums[-1]
fib_num = fib(10)
print(fib_num)