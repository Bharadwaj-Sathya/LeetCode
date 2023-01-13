# A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
# Each of the words consists of only uppercase and lowercase English letters (no punctuation).

# Example 1:

# Input: s = "Hello how are you Contestant", k = 4
# Output: "Hello how are you"
# Explanation:
# The words in s are ["Hello", "how" "are", "you", "Contestant"].
# The first 4 words are ["Hello", "how", "are", "you"].
# Hence, you should return "Hello how are you".

class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        return ' '.join(s.split()[:k])


sol = Solution()
print(sol.truncateSentence('Hello how are you Contestant', 4))
print(sol.truncateSentence('What is the solution to this problem', 4))
print(sol.truncateSentence('chopper is not a tanuki', 5))

