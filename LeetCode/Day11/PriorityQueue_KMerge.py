from queue import PriorityQueue

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def merge_k_lists(lists):
    dummy = ListNode(None)
    curr = dummy
    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val, node))
    while not q.empty():
        curr.next = q.get()[1]  # These two lines seem to
        curr = curr.next  # be equivalent to :-   curr = q.get()[1]
        if curr.next:
            q.put((curr.next.val, curr.next))
    return dummy.next

# Driver code
if __name__ == '__main__':
    data = [[1,2,5,7],
             [2,4,6,8],
             [0,9,10,11]]
    lists = []
    for nums in data:
        node = ListNode(nums[0])
        temp = node
        for i in range(1, len(nums)):
            new_node = ListNode(nums[i])
            temp.next = new_node
            temp = temp.next
        lists.append(node)
    # TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
    print(merge_k_lists(lists))

