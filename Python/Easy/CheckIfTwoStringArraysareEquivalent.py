# Given two string arrays word1 and word2, return true if the two arrays represent the same string, and false otherwise.
# A string is represented by an array if the array elements concatenated in order forms the string.
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        str1 = ''.join(word1)
        str2 = ''.join(word2)
        if str1 == str2:
            return True
        else:
            return False


sol = Solution()
print(sol.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
print(sol.arrayStringsAreEqual( ["a", "cb"], ["ab", "c"]))
print(sol.arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"]))
