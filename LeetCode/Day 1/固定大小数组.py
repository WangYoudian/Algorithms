import array 

# initializing array with array values 
# initializes array with signed integers 
arr= array.array('i',[1, 2, 3, 1, 5]) 

# printing original array 
print("The new created array is : ",end="") 
for i in range(len(arr)): 
	print(arr[i],end=" ")

print()

# using pop() to remove element at 2nd position 
print("The popped element is : ",end="") 
print(arr.pop(2)); 

# printing array after popping 
print("The array after popping is : ",end="") 
for i in range(len(arr)): 
	print(arr[i],end=" ")

print() 

# using remove() to remove 1st occurrence of 1 
arr.remove(1)

# printing array after removing 
print ("The array after removing is : ",end="") 
for i in range(len(arr)): 
	print(arr[i],end=" ")

print()

# using insert() to insert 6 after the 2nd position 
# parameters[0] means position, followed by a value
arr.insert(2, 6)

# printing array after inserting 
print ("The array after inserting is : ",end="") 
for i in range(len(arr)): 
	print(arr[i],end=" ")

print()
