class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class Stack:
	def __init__(self):
		self.head = None

	def isEmpty(self):
		if self.head == None:
			return False
		return True

	def push(self, data):
		if self.head == None:
			self.head = Node(data)
			return 
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def pop(self):
		if self.head == None:
			return None
		popped = self.head.data
		self.head = self.head.next
		return popped

	def peek(self):
		if self.head == None:
			print('The stack is empty!')
			return None

	def display(self):
		if self.head == None:
			return None
		temp = self.head
		while temp:
			print(temp.data)
			temp = temp.next
		print('Display finished!')

stack = Stack()
stack.push(10)
stack.push(20)
p1 = stack.pop()
n1 = stack.peek()
is_empty = stack.isEmpty()
stack.display()