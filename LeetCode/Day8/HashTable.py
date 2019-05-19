# 构造哈希表的单个节点
class Node:
	def __init__(self, key, value):
		# self.hnext在Python中直接是列表的index体现
		# self.hnext = None
		self.data = (key, value)

# 构造哈希Map类，以及创建、插入、删除、查找方法
class ChainedHashMap:
	def __init__(self, size):
		self.size = size
		self.table = [[] for i in range(size)]

	def hash_func(self, key):
		return key%self.size

	def printMap(self):
		# 不是按照操作的顺序，而是按照节点在哈希Map中的存储顺序
		for i in range(self.size):
			for nodes in self.table[i]:
				print(nodes.data)

	def insert(self, key, value):
		new_node = Node(key, value)
		hash_key = self.hash_func(key)
		self.table[hash_key].append(new_node)

	def delete(self, key):
		hash_key = self.hash_func(key)
		for node in self.table[hash_key]:
			if node is None:
				print('Key:', key, ' is not in the table!')
				return			
			if node.data[0]==key:
				self.table[hash_key].remove(node)
				print('Delete successfully!')

	def search(self, key):
		# return the value of key as a list
		# if key has multiple values, then return all
		hash_key = self.hash_func(key)
		for node in self.table[hash_key]:
			# 没有节点
			# 有节点但是却没有该key
			# 查找到
			if node is None:
				print('Key:', key, ' is not in the table!')
				return			
			if node.data[0]==key:
				print('Key has been found!', f'The value for {key} is:', node.data[1])
				return
		print('Key:', key, ' is not in the table!')

if __name__ == '__main__':
	# driver code
	hashtable = ChainedHashMap(10)
	hashtable.insert(10, 'India')
	hashtable.insert(20, 'Nepal')
	hashtable.insert(25, 'America')
	hashtable.printMap()
	hashtable.delete(20)
	hashtable.search(10)