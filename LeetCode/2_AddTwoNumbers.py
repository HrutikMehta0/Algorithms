from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    predecesor = None
    x = 0
    while l1 is not None or l2 is not None or x != 0:
        if l1 is None and l2 is None:
            res = x
        elif l1 is None:
           res= x + 0 + l2.val
           l2 = l2.next
        elif l2 is None:
            res = x + l1.val + 0
            l1 = l1.next
        else:
            res = x + l1.val + l2.val
            l1 = l1.next
            l2 = l2.next
        x = int(res/10)
        predecesor = ListNode(int(res % 10), predecesor)

    result = None
    while predecesor is not None:
        next = predecesor.next
        predecesor.next = result
        result = predecesor
        predecesor = next
    return result
    # val = l1
    # j = 0
    # resl1 = 0
    # while val is not None:
    #     resl1 = resl1 + (pow(10, j) * val.val)
    #     val = val.next
    #     j += 1
    # resl2 = 0
    # val = l2
    # i = 0
    # while val is not None:
    #     resl2 = resl2 + (pow(10, i) * val.val)
    #     val = val.next
    #     i += 1
    #
    # if j > i:
    #     length = j
    # else:
    #     length = i
    # res = resl1 + resl2
    # predecesor = None
    # isFirst = True
    # while length >= 0:
    #     if isFirst and length != 1:
    #         if int((res / pow(10, length) % 10)) != 0:
    #             predecesor = ListNode(int((res / pow(10, length) % 10)), predecesor)
    #             isFirst = False
    #     else:
    #         predecesor = ListNode(int((res / pow(10, length) % 10)), predecesor)
    #     length = length - 1
    # return predecesor


# TEST CASE 1
l3 = ListNode(3, None)
l2 = ListNode(4, l3)
l1 = ListNode(2, l2)

ll3 = ListNode(4, None)
ll2 = ListNode(6, ll3)
ll1 = ListNode(5, ll2)

# TEST CASE 2
# l7 = ListNode(9, None)
# l6 = ListNode(9, l7)
# l5 = ListNode(9, l6)
# l4 = ListNode(9, l5)
# l3 = ListNode(9, l4)
# l2 = ListNode(9, l3)
# l1 = ListNode(9, l2)
#
# ll4 = ListNode(9, None)
# ll3 = ListNode(9, ll4)
# ll2 = ListNode(9, ll3)
# ll1 = ListNode(9, ll2)

# TEST CASE 3
# l1 = ListNode(0, None)
# ll1 = ListNode(1, None)
print(addTwoNumbers(l1, ll1).val)
