class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end='->')
			temp = temp.next

	def append(self, data):
		new_node = Node(data)

		if self.head == None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

# a and b are LinkedList class instance
def sortMerge(head1, head2):
	temp = None
	if head1 == None:
		return head2
	if head2 == None:
		return head1
	if head1.data <= head2.data:
		temp = head1
		temp.next = sortMerge(head1.next, head2)
	else:
		temp = head2
		temp.next = sortMerge(head1, head2.next)
	return temp

def mergeKLists(arr, last):
	while last!=0:
		i = 0
		j = last
		while i<j:
			arr[i].head = sortMerge(arr[i].head, arr[j].head)
			i += 1
			j -= 1
			if i>=j:
				last = j
	return arr[0].head

if __name__ == '__main__':
	k = 3
	arr = [LinkedList() for i in range(k)]

	arr[0].append(1)
	arr[0].append(3)
	arr[0].append(5)
	arr[0].append(7)

	arr[1].append(2)
	arr[1].append(4)
	arr[1].append(6)
	arr[1].append(8)

	arr[2].append(0)
	arr[2].append(9)
	arr[2].append(10)
	arr[2].append(11)

	llist = LinkedList()
	llist.head = mergeKLists(arr, k-1)

	llist.printList()
