class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputs = []
        temp = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                temp *= nums[j]
            outputs.append(temp)
            temp = 1
        return outputs