# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal substring consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        len_word = 0
        words = s.strip()

        for i in range(len(words)):
            if words[i] == " ":
                len_word = 0
            else:
                len_word += 1
        return len_word


sol = Solution()
print(sol.lengthOfLastWord("Hello World"))
print(sol.lengthOfLastWord("   fly me   to   the moon  "))
print(sol.lengthOfLastWord("luffy is still joyboy"))
