class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for n in range(1, len(s)):
            result += abs(ord(s[n]) - ord(s[n-1]))
        return result