def kthFactor(n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        i = 1
        count = 0
        while i <= n:
            if n % i == 0:
                count+=1
                if count == k:
                    return i
                i+=1
            else:
                i+=1
        return -1


# Test cases
print(kthFactor(12, 3)) #Output: 3
print(kthFactor(7, 2)) #Output: 7
print(kthFactor(4, 4)) #Output: -1