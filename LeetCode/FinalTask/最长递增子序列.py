# Dynamic programming Python implementation of LIS problem 
def lis(arr): 
	n = len(arr) 
	# Declare the list (array) for LIS and initialize LIS 
	# values for all indexes 
	lis = [1]*n 
	# Compute optimized LIS values in bottom up manner 
	for i in range (1 , n): 
		for j in range(0 , i): 
			if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
				lis[i] = lis[j]+1

	# Initialize maximum to 0 to get the maximum of all 
	# LIS 
	maximum = 0
	for i in range(n): 
		maximum = max(maximum , lis[i]) 
	return maximum 

# Driver program to test above function 
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
# 10,22,33,50,60
print("Length of LIS is", lis(arr))



# Binary search 
def GetCeilIndex(arr, T, l, r, key): 
	while (r - l > 1): 
		m = l + (r - l)//2
		if (arr[T[m]] >= key): 
			r = m 
		else: 
			l = m 
	return r 

def LongestIncreasingSubsequence(arr, n): 
	tailIndices =[0 for i in range(n + 1)] 

	# Initialized with -1 
	prevIndices =[-1 for i in range(n + 1)] 
	
	# it will always point 
	# to empty location 
	len = 1
	for i in range(1, n): 
		if (arr[i] < arr[tailIndices[0]]): 		
			# new smallest value 
			tailIndices[0] = i 
		
		elif (arr[i] > arr[tailIndices[len-1]]): 
		
			# arr[i] wants to extend 
			# largest subsequence 
			prevIndices[i] = tailIndices[len-1] 
			tailIndices[len] = i 
			len += 1
		
		else: 
			pos = GetCeilIndex(arr, tailIndices, -1, 
								len-1, arr[i]) 
			prevIndices[i] = tailIndices[pos-1] 
			tailIndices[pos] = i 		
	print("LIS of given input:") 
	i = tailIndices[len-1] 
	while(i >= 0): 
		print(arr[i], " ", end ="") 
		i = prevIndices[i] 
	print() 

	return len

# driver code 
arr = [ 2, 5, 3, 7, 11, 8, 10, 13, 6 ] 
n = len(arr) 

print("LIS size:\n", LongestIncreasingSubsequence(arr, n))