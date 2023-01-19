# Ion Flux Relabeling
# ===================
# #Oh no! Commander Lambda's latest experiment to improve the efficiency of the LAMBCHOP doomsday device has backfired
# spectacularly. The Commander had been improving the structure of the ion flux converter tree, but something went
# terribly wrong and the flux chains exploded. Some of the ion flux converters survived the explosion intact,
# but others had their position labels blasted off. Commander Lambda is having her henchmen rebuild the ion flux
# converter tree by hand, but you think you can do it much more quickly -- quickly enough, perhaps, to earn a promotion!

# Flux chains require perfect binary trees, so Lambda's design arranged the ion flux converters to form one.
# To label them, Lambda performed a post-order traversal of the tree of converters and labeled each converter
# with the order of that converter in the traversal, starting at 1. For example, a tree of 7 converters
# would look like the following:
#
#    7
#  3   6
# 1 2 4 5
#
# Write a function solution(h, q) - where h is the height of the perfect tree of converters and q is a list of positive
# integers representing different flux converters - which returns a list of integers p where each element in p is the
# label of the converter that sits on top of the respective converter in q, or -1 if there is no such converter.
# For example, solution(3, [1, 4, 7]) would return the converters above the converters at indexes 1, 4, and 7 in a
# perfect binary tree of height 3, which is [3, 6, -1].
#
# The domain of the integer h is 1 <= h <= 30, where h = 1 represents a perfect binary tree containing only the root,
# h = 2 represents a perfect binary tree with the root and two leaf nodes, h = 3 represents a perfect binary tree
# with the root, two internal nodes and four leaf nodes (like the example above), and so forth.
# The lists q and p contain at least one but no more than 10000 distinct integers, all of which will
# be between 1 and 2^h-1, inclusive.
def solution(h, q):
    arr = [int(iterSolution(h, x)) for x in q]
    return arr


def iterSolution(h, x):
    curr_root = 2 ** h - 1
    # base case
    if x == curr_root:
        return -1
    half = (curr_root + 1) / 2
    if x == half - 1 or x == curr_root - 1:
        return curr_root
    if x < half:
        return iterSolution(h - 1, x)
    else:
        half -= 1
        return iterSolution(h - 1, x - half) + half


# # Test cases
print(solution(3, [7, 3, 5, 1]))
print(solution(5, [i for i in range(1, 32)]))
