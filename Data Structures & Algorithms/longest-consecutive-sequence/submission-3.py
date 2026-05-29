class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)

        for i in nums:
            streak = 0
            num = i
            while num in store:
                streak += 1
                num += 1
            res = max(streak, res)
        return res