from typing import List


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to .
# target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_len = len(nums)
        for i in range(0, nums_len):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i, j]


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))
print(sol.twoSum([3, 2, 4], 6))
print(sol.twoSum([3, 3], 6))
print(sol.twoSum([2,5,5,11], 10))
