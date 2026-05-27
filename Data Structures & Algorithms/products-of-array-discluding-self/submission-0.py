class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = []
        result = []
        temp = 0

        #prefix
        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[i])
                temp = nums[i]
            else:
                temp = nums[i] * temp
                prefix.append(temp)

        #postfix
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                postfix.append(nums[i])
                temp = nums[i]
            else:
                temp = nums[i] * temp
                postfix.append(temp)

        postfix.reverse()
        #result
        for i in range(len(nums)):
            if i == 0:
                temp = 1 * postfix[i+1]
                result.append(temp)
            elif i == len(nums)-1:
                temp = 1 * prefix[i-1]
                result.append(temp)
            else:
                temp = prefix[i-1] * postfix[i+1]
                result.append(temp)
        return result