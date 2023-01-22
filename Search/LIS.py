def lis(A):
    L = [1] * len(A)
    for i in range(1, len(L)):
        subproblems = [L[j] for j in range(i) if A[j] < A[i]]
        L[i] = 1 + max(subproblems, default=0)
    return max(L, default=0)