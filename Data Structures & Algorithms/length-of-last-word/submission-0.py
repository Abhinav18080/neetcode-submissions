class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s) == 0:
            return 0
        stripped_s = s.strip()
        stripped_s = stripped_s.split()[-1]
        return len(stripped_s)