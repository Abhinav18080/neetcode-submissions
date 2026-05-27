class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nodupnums = list(set(nums))
        count = {}
        result = []
        counter = 0

        for i in nodupnums:
            numtimes = nums.count(i)
            count[i] = numtimes
        
        sorted_dict_asc = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        for key,value in sorted_dict_asc.items():
            result.append(key)
            counter += 1
            if counter >= k:
                break
        return result