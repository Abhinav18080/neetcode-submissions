class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a dictionary where the key is the numbers in nums
        # and values would be the count of those individual numbers
        sortednums = list(set(nums))
        result = []
        dictstore = {}
        for i in range(len(sortednums)):
            dictstore[sortednums[i]] = nums.count(sortednums[i])
        #after doing that, sort the list in ascending order
        #based on the values
        sorted_dict = dict(sorted(dictstore.items(), key=lambda item: item[1]))
        #then pick the last k values and put it in an array and 
        #return that
        print(sorted_dict)
        print(dictstore)
        while(k != 0):
            key, value = sorted_dict.popitem()
            result.append(key)
            k -= 1
        return sorted(result)