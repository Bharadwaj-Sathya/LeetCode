# You are given a large integer represented as an integer array digits, where each digits[i]
# is the ith digit of the integer. The digits are ordered from most significant to least significant in
# left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ''.join(map(str, digits))
        int_num = int(str_num) + 1
        return list(map(int, str(int_num)))


sol = Solution()
print(sol.plusOne([1, 2, 3]))
print(sol.plusOne([4, 3, 2, 1]))
print(sol.plusOne([9]))
