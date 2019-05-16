from copy import copy
import random
import time

def getMinKthByBFPRT(arr, k):
    copyArray = arr.copy()
    return select(copyArray, 0, len(copyArray)-1, k-1)  #k-1 is the sub index of arr element

def select(arr, begin, end, i):
    if begin == end:
        return arr[begin]
    pivot = medianOfMedians(arr, begin, end)
    #=pivot? from pivotRange[0] to pivotRange[1]
    pivotRange = partition(arr, begin, end, pivot)
    if i >= pivotRange[0] and i <= pivotRange[1]:
        return arr[i]
    elif i < pivotRange[0]:
        return select(arr, begin, pivotRange[0]-1, i)
    else:
        return select(arr, pivotRange[1]+1, end, i)

# pay attention to the boundary
def medianOfMedians(arr, begin, end):
    cnt = end - begin + 1
    if cnt % 5 == 0:
        offset = 0
    else:
        offset = 1
    mArr = [0] * (cnt//5 + offset)
    for i in range(len(mArr)):
        beginI = begin + i*5
        endI = beginI + 4
        mArr[i] = getMedian(arr, beginI, min(endI, end))
    return select(mArr, 0, len(mArr)-1, len(mArr)//2)

#return a range of nums which equal to pivot value 
def partition(arr, begin, end, pivotValue):
    small = begin - 1
    cur = begin
    big = end + 1
    #normalize the break condition
    while cur != big:
        if arr[cur] < pivotValue:
            swap(arr, small+1, cur)
            small += 1
            cur += 1
        elif arr[cur] > pivotValue:
            swap(arr, cur, big-1)  #big out of index
            big -= 1
        else:
            cur += 1
    return [small+1, big-1]

def getMedian(arr, begin, end):
    insertionSort(arr, begin, end)
    ceil = begin + end
    return arr[ceil//2 + ceil%2]

def insertionSort(arr, begin, end):
    for i in range(begin, end+1):
        for j in range(i, begin, -1):
            if arr[j-1] > arr[j]:
                #swap a[j] and a[j-1]
                arr[j-1], arr[j] = arr[j], arr[j-1]
            else:
                break

def swap(arr, index1, index2):
    arr[index1], arr[index2] = arr[index2], arr[index1]

def main(arr):
    #for test
    k = 10
    num = getMinKthByBFPRT(arr, k)
    print(arr)
    print(num)
    print(sorted(arr)[k-1])

if __name__ == '__main__':
    arr = list(map(lambda x:random.randint(0, 1000), list(range(100))))
    start = time.clock()
    main(arr)
    end = time.clock()
    print('Program costs %.6f s' %(end-start))
