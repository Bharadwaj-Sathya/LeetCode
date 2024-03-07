from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        # Iterate through characters of the first string
        for i in range(len(strs[0])):
            # Check if character matches in all strings
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:
                    return strs[0][:i]  # Return the prefix up to this point
        return strs[0]


sol = Solution()
strs1 = ["flower", "flow", "flight"]
print(sol.longestCommonPrefix(strs1))  # Output: "fl"

strs2 = ["dog", "racecar", "car"]
print(sol.longestCommonPrefix(strs2))  # Output: ""
