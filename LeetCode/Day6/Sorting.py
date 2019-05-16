def bubble_sort(lis):
    """
    Bubble Sorting algorithm

    :param lis: list of values to sort
    :return: sorted values
    """
    for i in range(len(lis)):
        for j in range(len(lis) - 1, i, -1):
            if lis[j] < lis[j - 1]:
                lis[j], lis[j - 1] = lis[j - 1], lis[j]
    return lis

def bucket_sort(lis, bucket_size=5):
    """
    bucket sort algorithm
    
    :param lis: list of values to sort
    :param bucket_size: Size of the bucket
    :return: sorted values
    """
    string = False

    if len(lis) == 0:
        # print("You don\'t have any elements in array!")
        raise ValueError("Array can not be empty.")
    
    elif all(isinstance(element, str) for element in lis):
        string = True
        lis = [ord(element) for element in lis]

    min_value = lis[0]
    max_value = lis[0]

    # For finding minimum and maximum values
    for i in range(0, len(lis)):
        if lis[i] < min_value:
            min_value = lis[i]
        elif lis[i] > max_value:
            max_value = lis[i]

    # Initialize buckets
    bucket_count = math.floor((max_value - min_value) / bucket_size) + 1
    buckets = []
    for i in range(0, int(bucket_count)):
        buckets.append([])

    # For putting values in buckets
    for i in range(0, len(lis)):
        # TODO: floor expects floats but could be receiving int or slice
        buckets[math.floor(float((lis[i] - min_value) / bucket_size))].append(lis[i])

    # Sort buckets and place back into input array
    sorted_array = []
    for i in range(0, len(buckets)):
        insertion_sort.sort(buckets[i])
        for j in range(0, len(buckets[i])):
            sorted_array.append(buckets[i][j])

    if string:
        return [chr(element) for element in sorted_array]
    else:
        return sorted_array

def counting_sort(lis):
    """
    counting sort algorithm
    
    :param lis: list of values to sort
    :return: sorted values
    """
    try:
        max_value = 0
        for i in range(len(lis)):
            if lis[i] > max_value:
                max_value = lis[i]

        buckets = [0] * (max_value + 1)

        for i in lis:
            buckets[i] += 1
        i = 0

        for j in range(max_value + 1):
            for a in range(buckets[j]):
                lis[i] = j
                i += 1

        return lis

    except TypeError as error:
        print('Counting Sort can only be applied to integers. {}'.format(error))

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

def insertion_sort(lis):
    """
    Insertion sort algorithm

    :param lis: list or values to sort
    :return: sort values
    """
    for i in range(1, len(lis)):
        current_number = lis[i]
        for j in range(i - 1, -1, -1):
            if lis[j] > current_number:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]
            else:
                lis[j + 1] = current_number
                break
    return lis

def merge_sort(lis):
    """
    Function to sort an array 
    using merge sort algorithm 
    
    :param lis: list of values to sort
    :return: sorted
    """
    if len(lis) == 0 or len(lis) == 1:
        return lis
    else:
        middle = len(lis)//2
        a = sort(lis[:middle])
        b = sort(lis[middle:])
        return merge(a, b)
def merge(a, b):
    """
    Function to merge 
    two arrays / separated lists
    
    :param a: Array 1
    :param b: Array 2
    :return: merged arrays
    """
    c = []
    while len(a) != 0 and len(b) != 0:
        if a[0] < b[0]:
            c.append(a[0])
            a.remove(a[0])
        else:
            c.append(b[0])
            b.remove(b[0])
    if len(a) == 0:
        c += b
    else:
        c += a
    return c

def quick_sort(lis):
    """
    quick_sort algorithm
    :param lis: list of integers to sort
    :return: sorted list
    """
    if len(lis) <= 1:
        return lis
    pivot = lis[len(lis) // 2]
    left = [x for x in lis if x < pivot]
    middle = [x for x in lis if x == pivot]
    right = [x for x in lis if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def selection_sort(lis):
    """
    selection sort algorithm
    
    :param lis: list of integers to sort
    :return: sorted list
    """

    # For iterating n - 1 times
    for i in range(len(lis) - 1):
        minimum = i

        # Compare i and i + 1 element
        for j in range(i + 1, len(lis)):
            if lis[j] < lis[minimum]:
                minimum = j
        if minimum != i:
            lis[i], lis[minimum] = lis[minimum], lis[i]
    return lis

def shell_sort(lis):
    """
    Shell sort algorithm

    :param lis: list of integers to sort
    :return: sorted list
    """
    gap = len(lis) // 2
    while gap > 0:
        for i in range(gap, len(lis)):
            current_item = lis[i]
            j = i
            while j >= gap and lis[j - gap] > current_item:
                lis[j] = lis[j - gap]
                j -= gap
            lis[j] = current_item
        gap //= 2

    return lis