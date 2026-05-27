class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result = list(set(nums))
        return len(result) != len(nums)