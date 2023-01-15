def kthSmallest(H,k):
    for i in range(0, k):
        min = extractMin(H)
    return min

def extractMin(H):
    #find the root x with minimum key in the root list of H, and remove x from the root list of H
    H1 = makeBinomialHeap()
    #reverse the order of the super list of x's children and set First[H1] to point the head of resulting list
    H = union(H, H1)
    return x


def union(H, H1):
    # Step 1: Merge H and H1. Then Link the roots of H1 and H in non-decreasing order
    # Step 2: Restore the Binomial Heap by linking binomial trees of same degree together,
    # traverse the super-list, keeping track of first, current and succesor pointers. (This takes O(lgn) time in our case)
    prev = None
    x = H.First()
    while x is not None:
        if degree[x] != degree[successor(x)] or sibling(successor(x)) != None and degree[sibiling(successor(x))] == degree[x]:
            prev = x
            x = successor(x)
       # else if key[x] <= key[successor(x)]:
          #  sibiling(x) = sibiling(successor(x))
            BinomialLink(successor(x), x)
      #  else if prev is None:
        #    H.First() = succesor(x)
        else:
         #   sibiling(prev) = successor(x)
            BinomialLink(x, successor(x))
            x = successor(x)
      #  successor(x) = sibiling(x)
    return H

