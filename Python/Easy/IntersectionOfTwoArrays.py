# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result
# must be unique and you may return the result in any order.

# Example 1:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for i in nums1:
            if i in nums2:
                if i not in nums3:
                    nums3.append(i)
        return nums3


sol = Solution()
print(sol.intersection([1, 2, 2, 1], [2, 2]))
print(sol.intersection([4, 9, 5], [9, 4, 9, 8, 4]))
