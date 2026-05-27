class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(t) != len(s)):
            return False
        temp_s = list(set(s))
        for i in temp_s:
            if (i not in t) or s.count(i) != t.count(i):
                return False
        return True