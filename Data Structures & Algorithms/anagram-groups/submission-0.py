class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        alreadychecked = [False] * len(strs)
        for i in range(len(strs)):
            if not alreadychecked[i]:
                temp = [strs[i]]
                alreadychecked[i] = True
                for j in range(i+1, len(strs)):
                    if not alreadychecked[j] and (sorted(strs[i].lower()) == sorted(strs[j].lower())):
                        temp.append(strs[j])
                        alreadychecked[j] = True
                anagrams.append(temp)
        return anagrams