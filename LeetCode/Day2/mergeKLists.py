class LinkedList:
	def __init__(self, data):
		self.data = data
		self.next = None

def printList(head):
	while head != None:
		print(head.data)
		head = head.next

def getLength(head):
	cnt = 0
	while head != None:
		cnt += 1
		head = head.next
	return cnt

# RecursionError: maximum recursion depth exceeded
# a and b are two linked lists
def sortMergeRecur(a, b):
	result = LinkedList(None)
	if a == None:
		return b
	if b == None:
		return a

	# pick either a or b, and recur
	if a.data <= b.data:
		result = a
		result.next = sortMerge(a, b)
	else:
		result = b
		result.next = sortMerge(a, b)

	return result

def sortMerge(a, b):
	head = LinkedList(None)
	temp = head
	if a == None:
		return b
	if b == None:
		return a
	while a!=None and b!=None:
		if a.data <= b.data:
			# temp.data = a.data
			temp = a
			print(temp.data)
			temp = temp.next
			a = a.next
		else:
			# temp.data = b.data
			temp = b
			print(temp.data)
			temp = temp.next
			b = b.next

	if a != None:
		temp = a
	if b != None:
		temp = b
	return head



# arr stores array of linked lists
# last means how many list(s) are/is left
def mergeKLists(arr, last):
	while last != 0:
		i = 0
		j = last
		# K/2 every round until there is only one list left
		while i<j:
			# arr[i] = sortMergeRecur(arr[i], arr[j])
			arr[i] = sortMerge(arr[i], arr[j])
			i += 1
			j -= 1
			if i >= j:
				last = j
	return arr[0]

if __name__ == '__main__':
	k = 3
	arr = [None for i in range(k)]

	arr[0] = LinkedList(1)
	arr[0].next = LinkedList(3)
	arr[0].next.next = LinkedList(5)
	arr[0].next.next.next = LinkedList(7)

	arr[1] = LinkedList(2)
	arr[1].next = LinkedList(4)
	arr[1].next.next = LinkedList(6)
	arr[1].next.next.next = LinkedList(8)

	arr[2] = LinkedList(0)
	arr[2].next = LinkedList(9)
	arr[2].next.next = LinkedList(10)
	arr[2].next.next.next = LinkedList(11)

	# printList(arr[0])

	head = mergeKLists(arr, k-1)

	printList(head)
