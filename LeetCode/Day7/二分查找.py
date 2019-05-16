def binary_search(_list, target):
    if type(_list) is not list:
        raise TypeError("binary search only excepts lists, not {}".format(str(type(_list))))
    # First position of the list
    left = 0
    # Last position of the list
    right = len(_list) - 1
    try:
        while left <= right:
            mid = (left + right) // 2
            if target == _list[mid]:
                return mid
            elif target < _list[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
    except TypeError:
        return False