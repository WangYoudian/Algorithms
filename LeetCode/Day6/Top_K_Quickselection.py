def select(array, left, right, n):
    """
    Recursively defined function for finding nth number in unsorted list

    :param array:
    :param left:
    :param right:
    :param n:
    :return:
    """
    if left == right:
        return array[left]
    split = partition(array, left, right, n)
    length = split - left + 1
    if length == n:
        return array[split]
    elif n < length:
        return select(array, left, split - 1, n)
    else:
        return select(array, split + 1, right, n - length)


def partition(array, left, right, pivot):
    """
    helper method for select functions
    :param array:
    :param left:
    :param right:
    :param pivot:
    :return:
    """
    pivot_val = array[pivot]
    array[pivot], array[right] = array[right], array[pivot]
    store_index = left

    for i in range(left, right):
        if array[i] < pivot_val:
            array[store_index], array[i] = array[i], array[store_index]
            store_index += 1

    array[right], array[store_index] = array[store_index], array[right]
    return store_index
