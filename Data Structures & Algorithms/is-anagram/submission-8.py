class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            letter = s[i]
            if letter not in t or t.count(letter) != s.count(letter):
                return False
        return True