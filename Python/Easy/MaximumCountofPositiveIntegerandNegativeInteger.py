# Given an array nums sorted in non-decreasing order, return the maximum between the number of positive integers and
# the number of negative integers.

# In other words, if the number of positive integers in nums is pos and the number of negative integers is neg,
# then return the maximum of pos and neg.

# Note that 0 is neither positive nor negative.


from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        for i in nums:
            if i < 0:
                neg += 1
            if i > 0:
                pos += 1
        return max(pos, neg)


sol = Solution()
print(sol.maximumCount([-2,-1,-1,1,2,3]))
print(sol.maximumCount([-3,-2,-1,0,0,1,2]))
