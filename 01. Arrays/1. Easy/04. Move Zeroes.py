# https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(nums):
        
        """
        Zero is the pointer to the elements which have a value 0.
        If we find any non-zero element, then, we swap it with the zero position value, and we increment the value of zero.
        """
        
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
        return nums
                
sol = Solution
print(sol.moveZeroes([0,1,0,3,12]))


"""
Time Complexity - 0(n)

Space Complexity - 0(1)
"""