# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
# missing from the array.
from typing import List


# Example 1:

# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number
# in the range since it does not appear in nums.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        len_n = len(nums)
        res = len_n

        for i in range(len_n):
            res ^= i ^ nums[i]

        return res

sol = Solution()
print(sol.missingNumber([3,0,1]))
print(sol.missingNumber([0,1]))
print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))
