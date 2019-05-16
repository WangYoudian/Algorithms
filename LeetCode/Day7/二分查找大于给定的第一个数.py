def vague_binary_search(lis, target):
    if type(lis) is not list:
        raise TypeError("binary search only excepts lists, not {}".format(str(type(lis))))
    # First position of the list
    left = 0
    # Last position of the list
    right = len(lis) - 1
    try:
        while left <= right:
            mid = (left + right) // 2
            if target == lis[mid]:
                if mid+1 <= len(lis):
                    return mid+1
                    # return lis[mid+1]
                else:
                    return False
            elif target < lis[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return False
    except TypeError:
        return False