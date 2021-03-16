"""
Given an unsorted integer array nums, find the smallest missing positive integer.

Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
"""

version1 

class Solution:
    def firstMissingPositive(self,nums:List[int]) -> int:
        ans = 1
        if 1 not in nums:
            return ans
        for i in range (len(nums)):
            if ans in nums:
                ans+=1
        return ans

version2
class Solution:
    def firstMissingPositive(self, nums:List[int])-> int:
        nums_set = set(nums)
        for i range(1,len(nums)+2):
            if i not in nums_set:
                return i
