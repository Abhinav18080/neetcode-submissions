class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sAlpha = "".join(sorted(s))
        tAlpha = "".join(sorted(t))
        return sAlpha == tAlpha