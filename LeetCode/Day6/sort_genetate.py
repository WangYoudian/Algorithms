# Dependency:
# pip install pygorithm

from pygorithm import sorting
# print(dir(sorting))
# 'bubble_sort', 'bucket_sort', 'counting_sort', 'heap_sort', 'insertion_sort', 'merge_sort', 'quick_sort', 'selection_sort', 'shell_sort'

# algo1 = sorting.bubble_sort.get_code()
# print(algo1)

func_paras = dir(sorting)
for i in range(10, len(func_paras)):
	# Calling a function of a module by using its name (a string)
	# What's more, if func_paras[i] is a function, then replace .get_code() with ()
	code = getattr(sorting, func_paras[i]).get_code()
	print(code)
