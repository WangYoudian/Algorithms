# from heapq import heapify
def heap_sort(lis):
    """
    heap sort algorithm

    :param lis: list of values to sort
    :return: sorted values
    """
    # TODO: Add description of how this works!
    
    # create the heap
    heapify(lis)              
    end = len(lis) - 1
    while end > 0:
        lis[end], lis[0] = lis[0], lis[end]
        shift_down(lis, 0, end - 1)
        end -= 1
    return lis
    
def heapify(lis):
    """
    function helps to maintain the heap property
    
    :param _list: list of values to sort
    :return: sorted values
    """

    start = len(_list) // 2
    while start >= 0:
        shift_down(_list, start, len(_list) - 1)
        start -= 1

def shift_down(lis, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        # right child exists and is greater than left child
        if child + 1 <= end and _list[child] < _list[child + 1]:
            child += 1
        # if child is greater than root(parent), then swap their positions
        if child <= end and _list[root] < _list[child]:
            _list[root], _list[child] = _list[child], _list[root]
            root = child
        else:
            return
