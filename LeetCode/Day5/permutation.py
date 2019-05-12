def permutation(lst): 
	if len(lst) == 0: 
		return [] 
	if len(lst) == 1: 
		return [lst] 

	l = [] 

	# Iterate the input(lst) and calculate the permutation 
	for i in range(len(lst)):
		m = lst[i] 

		remLst = lst[:i] + lst[i+1:] 

		# Generating all permutations where m is first element
		for p in permutation(remLst): 
			l.append([m] + p) 
	return l 


# Driver program to test above function 
data = list('123') 
for p in permutation(data): 
	print(p)

from itertools import permutations 
l = list(permutations(range(1, 4)))
print(l)
# <itertools.permutations object at 0x000001DC89F12E60>
# print(permutations(range(1, 4)))