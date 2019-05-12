from collections import deque

def printMax(arr, size, k):
	# define a window whose size=k
	Qi = deque(maxlen=k)
	for i in range(k):
		while Qi and arr[i]>=arr[Qi[-1]]:
			# if bigger number enters, make sure it in place
			Qi.pop()
		# store index that may be useful latter on
		Qi.append(i)
	for i in range(k, size):
		print(arr[Qi[0]], end=' ')
		while Qi and Qi[0]<=i-k:
			# remove indexes that are out of window
			# that is, it's totally useless
			Qi.popleft()
		while Qi and arr[i]>=arr[Qi[-1]]:
			Qi.pop()
		Qi.append(i)
	# print the maximum of the last window
	print(arr[Qi[0]])

if __name__ == '__main__':
	arr = [12, 1, 78, 90, 57, 89, 56] 
	size = len(arr)
	k = 3
	printMax(arr, size, k)