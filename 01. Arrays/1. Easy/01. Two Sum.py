# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(nums, target):
        
        Hashmap = {}
        
        """ We know, a+b = target, 
        so now, a = target - b """
    
        for index, value in enumerate(nums):
            key = target - value
            
            if key in Hashmap:
                return [Hashmap[key],index]
            else:
                Hashmap[value] = index
                
sol = Solution
print(sol.twoSum([2,7,11,15], 9))

"""
Time Complexity - 0(n)
We are traversing over all the elements one by one.   


Space Complexity - 0(n)
The keys are stored in a hashmap, so it takes 0(n) to store them and constant time 0(1) to fetch them.
"""