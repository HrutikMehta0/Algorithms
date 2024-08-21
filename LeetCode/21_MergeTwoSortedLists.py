class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            current = list1
            list1 = list1.next
        else:
            current.next = list2
            current = list2
            list2 = list2.next

    current.next = list1 if list1 else list2
    return dummy.next
        




# Test Cases
# Test Case 1
ln = ListNode(1)
ln.next = ListNode(2)
ln.next.next = ListNode(4)
ln2 = ListNode(1)
ln2.next = ListNode(3)
ln2.next.next = ListNode(4)
# Expected: 1 -> 1 -> 2 -> 3 -> 4 -> 4
print(mergeTwoLists(ln, ln2))


