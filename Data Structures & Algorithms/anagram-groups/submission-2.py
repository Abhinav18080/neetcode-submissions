class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        for i in strs:
            sortedstr = "".join(sorted(i))
            if sortedstr not in dictionary:
                dictionary[sortedstr] = []
                dictionary[sortedstr].append(i)
            else:
                dictionary[sortedstr].append(i)
        result = []
        for val in dictionary.values():
            result.append(val)
        return result