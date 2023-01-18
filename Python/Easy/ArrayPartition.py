# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.


from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum([i for i in nums[::2]])


sol = Solution()
print(sol.arrayPairSum([1,4,3,2]))
print(sol.arrayPairSum([6,2,6,5,1,2]))

