# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.
from typing import List


# Example 1:

# Input: nums = [2,2,1]
# Output: 1


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        size = len(nums)
        res = nums[0]

        for i in range(1, size):
            res = res ^ nums[i]

        return res


sol = Solution()
print(sol.singleNumber([2, 2, 1]))
print(sol.singleNumber([4, 1, 2, 1, 2]))
print(sol.singleNumber([3]))
