# https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(nums1, m, nums2, n):
        
        """
        Here, both the arrays are sorted arrays, so we're the filling the nums1 array backwards.
        We are matching the last elements of both the arrays first, and then filling the largest element in the last position.
        """
        
        a, b, pos = m -1, n - 1, m + n -1
        
        while b >= 0:
            if a >= 0 and nums1[a] > nums2[b]:
                nums1[pos] = nums1[a]
                a -= 1
            else:
                nums1[pos] = nums2[b]
                b -= 1
            pos -= 1
        return nums1

sol = Solution
print(sol.merge([1,2,3,0,0,0], 3, [2, 5, 6],3))


"""
Time Complexity - 0(m+n)

Space Complexity - 0(1)
"""