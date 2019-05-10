def firstMissingPositive(arr, size):
	for i in range(size):
		# abs(arr[i])-1<size
		# 1.avoid list index out of range;2.ignore number which is greater than size
		# arr[abs(arr[i])-1]>0
		# a map function to locate the index value which equals to abs(arr[i])
		# abs(arr[i])	and 	>0
		# in case arr[k] has been visited and set to negtive
		if abs(arr[i])-1<size and arr[abs(arr[i])-1]>0:
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
	for i in range(size):
		if arr[i] > 0:
			# indexes start at 0 but positive nums start at 1
			return i+1
	return size+1


def segragate(arr, size):
	j = 0
	for i in range(size):
		if arr[i] <= 0:
			# swap arr[i] and arr[j]
			arr[i], arr[j] = arr[j], arr[i]
			j += 1
	return j

def firstMissing(arr, size):
	shift = segragate(arr, size)
	return firstMissingPositive(arr[shift:], size-shift)

import random
# generate a random array
size = 20
arr = list(map(lambda x:random.randrange(-10, 10), list(range(size))))
print(sorted(arr))
print(arr)
leastPositive = firstMissing(arr, size)
print(leastPositive)