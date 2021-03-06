# 循环链表即在单链表的基础上
# 在LinkedList类的构造方法中添加一个指向头结点的尾节点

# Node class 
class Node: 
	def __init__(self, data): 
		# data->data domain; next->pointer domain
		self.data = data 
		self.next = None 

# Linked List class 
class LinkedList: 
	def __init__(self):
		# with a head node
		self.head = None
		self.rear = self.head

	# print a linked list
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
	
	# insert a new node at the beginning of linked list	
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# insert after a node
	def insertAfter(self, prev_node, new_data):
		# Why use is? Just think about it! And what's wrong with '=='
		if prev_node is None:
			print('The given previous node must exist!')
			return
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node	

	# append a node in the end of linked list
	def append(self, new_data):
	 	new_node = Node(new_data)
	 	if self.head is None:
	 		self.head = new_node
	 		return
	 	last = self.head
	 	while last.next:
	 		last = last.next
	 	last.next = new_node

	def remove(self, data):
	 	if self.head is None:
	 		print('This is an empty linked list. Remove data failed!')
	 		return
	 	node = self.head
	 	while node.data != data:
	 		prev_node = node
	 		node = node.next
	 	# node.data == data or node is None
	 	if node is None:
	 		print('Data not exist in linked list. Remove data failed!')
	 	prev_node.next = node.next
	 	del node
	 	return
