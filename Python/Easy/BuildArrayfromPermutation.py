# Given a zero-based permutation nums (0-indexed), build an array ans of the same length where ans[i] = nums[nums[i]]
# for each 0 <= i < nums.length and return it.
from typing import List


# A zero-based permutation nums is an array of distinct integers from 0 to nums.length - 1 (inclusive).


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums)):
            res.append(nums[nums[i]])
        return res


sol = Solution()
print(sol.buildArray([0,2,1,5,3,4]))
print(sol.buildArray([5,0,1,2,3,4]))
