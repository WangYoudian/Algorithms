'''
Author: Wang Youdian
Design Pattern: Factory Model
'''

# 含有hnext拉链指针域、双向有序链表指针域、数据域的节点
# 一共四个域，但实际只用到三个
class Node:
	def __init__(self, key, value):
		# self.hnext在Python中直接是列表的index体现
		# self.hnext = None
		self.next = None
		self.prev = None
		self.data = (key, value)

# 具有在表头插入节点、从头打印、删除节点的双向链表
class DeLinkedList:
	def __init__(self, cache_size):
		# has to be Node(None, None) or during initializing there will be 'no attribute' Error
		self.head = Node(None, None)
		self.rear = Node(None, None)
		self.cache_size = cache_size
		self.size = 0

	def printList(self):
		if self.head is None:
			print('The table is empty!')
			return False
		head = self.head
		while head != None:
			print(head.data)
			temp = head
			head = temp.next
		return True

	def overFlow(self):
		return self.size > self.cache_size

	def push(self, node):
		if self.head is None:
			self.head = node
			self.rear.next = self.head
			self.rear.prev = self.head
			self.head.next = self.rear
			self.head.prev = self.rear
			self.size += 1
			return True
		self.rear.next = node
		self.head.prev = node
		node.next = self.head		
		node.prev = self.rear
		self.head = node
		self.size += 1
		if self.overFlow():
			# print('Cache runs out of memory! Please initialize the table with a larger cache size!')
			# print('Or choose to ignore the warning with a cache size of %d', self.cache_size)
			self.head.prev = self.rear.prev
			self.rear.prev.next = self.head
			temp = self.rear
			self.rear = self.rear.prev
			del temp
		return True

	def delete(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
		
		del node
		self.size -= 1
		return True

	# 查找到了该key，将它移到表头
	# 这里是使用双向链表的原因——node的前驱是被需要的
	def modify(self, node):
		if node.next is None:
			self.push(node)
			return True

		node.prev.next = node.next
		node.next.prev = node.prev
		self.push(node)


# 使用链地址法解决哈希冲突的哈希表，作为缓存
# 包含的操作：插入、删除、查找
class LRUHashMap:
	def __init__(self, size, cache_size):
		self.size = size
		self.table = [[] for i in range(size)]
		self.cache = DeLinkedList(cache_size)

	# Standard Hashing using 'hash()'
	def hash_func(self, key):
		return hash(key)%self.size

	def printMap(self):
		# 不是按照操作的顺序，而是按照节点在哈希Map中的存储顺序
		for i in range(self.size):
			for nodes in self.table[i]:
				print(nodes.data)

	def printByTime(self):
		# 按照对象上一次操作离现在的时间长短，由最近到最久
		self.cache.printList()

	# def getByIndex(self, index):
	# 	# 时间上最近第index个插入或者查找的记录
	# 	# 注意：不是最近第index个操作的对象
	# 	# 对应了双向链表的第index个节点
	# 	pass

	def insert(self, key, value):
		new_node = Node(key, value)
		hash_key = self.hash_func(key)
		self.table[hash_key].append(new_node)
		# O(1) modification
		if self.search(key):
			self.cache.modify(new_node)
		return True

	def delete(self, key):
		hash_key = self.hash_func(key)
		for node in self.table[hash_key]:
			if node is None:
				print('Key:', key, ' is not in the table!')
				return False
			if node.data[0] == key:
				self.cache.delete(node)
				print('Delete successfully!')				
				return True

	def search(self, key):
		hash_key = self.hash_func(key)
		for node in self.table[hash_key]:
			if node is None:
				print('Key:', key, ' is not in the table!')
				return	False
			if node.data[0] == key:
				return node
		return False

	# 注：visit和search不同，visit和insert地位相等，访问cache
	# 而search则是加速链表查找
	def visit(self, key):
		if self.search(key):
			# node exists
			node = self.search(key)
			print('Key has been found!', f'The value for {key} is:', node.data[1])
			self.cache.modify(node)
			return True

		return False

# driver code
hashtable = LRUHashMap(10, 20)
hashtable.insert(10, 'India')
hashtable.insert(20, 'Nepal')
hashtable.insert(25, 'America')
hashtable.printMap()
hashtable.delete(20)
hashtable.search(10)
# 测试代码有些复杂，后面再补
# 测试的方面主要包含：
# 1.记录数量大于cache_size，即cache实例self.overFlow为True，这里再push的时候已经考虑了
# 2.visit的功能，注意区别于HashTable中实现的search功能。区别见注释