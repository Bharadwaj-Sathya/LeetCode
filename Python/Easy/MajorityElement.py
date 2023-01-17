# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority
# element always exists in the array.
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        counter = 0
        for val in nums:
            if counter == 0:
                candidate = val

            if candidate == val:
                counter += 1
            else:
                counter -= 1

        return candidate


sol = Solution()
print(sol.majorityElement([3,2,3]))
print(sol.majorityElement([2,2,1,1,1,2,2]))
