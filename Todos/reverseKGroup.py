# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Reverse Nodes in k-Group
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None

    def insert(self, v):
        if self.next is None:
            self.next = ListNode(v)
        else:
            print("Insertion failed!!")

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1 or head is None:
            return head
        pre_head = out = ListNode(0)
        out.next = head
        slow = quick = head
        while quick is not None:
            for _ in range(k):
                if quick is None:
                    # 长度小于k
                    return out.next
                # quick来到第k+1个节点
                quick = quick.next

            pre = quick
            _pre_head = slow
            for _ in range(k):
                # key point
                slow.next, pre, slow = pre, slow, slow.next
                print(slow.value, '\n', pre.value)
            pre_head.next = pre
            pre_head = _pre_head
        return out.next

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    head = ListNode(0)
    print(head)
    for i in arr:
        head.insert(i)
        print(i)
    temp = head
    # solution = Solution()
    # new_head = solution.reverseKGroup(head, 2)
    # temp = new_head
    while temp.next is not None:
        print(temp.value)
        temp = temp.next
