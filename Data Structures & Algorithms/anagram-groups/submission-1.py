class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for i in strs:
            sorted_i = sorted(i)
            newstr = "".join(sorted_i)
            if newstr not in hashmap:
                hashmap[newstr] = []
            hashmap[newstr].append(i)
        
        for key,value in hashmap.items():
            result.append(value)
        
        return result