# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
# representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
# accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be
# merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        elif m == 0:
            if len(nums2) > 0:
                for i in range(0,len(nums2)):
                    nums1[i] = nums2[i]
                nums1.sort()
                return nums1
            else:
                nums1[0] = nums2[0]
                return
        else:
            nums1[m:] = nums2
            nums1.sort()
            return nums1


sol = Solution()
print(sol.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(sol.merge([1], 1, [], 0))
print(sol.merge([0], 0, [1], 1))
print(sol.merge([1,2,3,0,0,0], 3, [2,5,6], 3))
print(sol.merge([1,2,4,5,6,0], 5, [3], 1))
