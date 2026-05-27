class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if(len(s) != len(t)):
            return False
        #loop through
        strs = list(set(s))
        strt = list(set(t))
        for i in range(len(strs)):
            if(strs[i] not in strt):
                return False
            elif(s.count(strs[i]) != t.count(strs[i])):
                return False
        return True