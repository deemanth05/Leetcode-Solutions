try:
    from math import gcd
except ImportError:
    from fractions import gcd  # Python 2 fallback

def get_lcm(a, b):
    return (a * b) // gcd(a, b)

class Solution(object):
    def findKthSmallest(self, coins, k):
        """
        :type coins: List[int]
        :type k: int
        :rtype: int
        """
        coins.sort()
        A = []
        for c in coins:
            if all(c % x != 0 for x in A):
                A.append(c)

        n = len(A)
        subsets = []
        for mask in range(1, 1 << n):
            cur_lcm = 1
            for j in range(n):
                if (mask >> j) & 1:
                    cur_lcm = get_lcm(cur_lcm, A[j])

            sign = 1 if (bin(mask).count('1') % 2 == 1) else -1
            subsets.append((cur_lcm, sign))

        def count_multiples(mid):
            return sum((mid // cur_lcm) * sign for cur_lcm, sign in subsets)

        # Explicit binary search
        low = 1
        high = A[0] * k

        while low < high:
            mid = (low + high) // 2
            if count_multiples(mid) >= k:
                high = mid
            else:
                low = mid + 1

        return low