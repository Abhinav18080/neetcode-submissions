class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r = m
        
        pivot = l

        def binarySearch(left: int, right: int) -> int:
            while left <= right:
                middle = (left + right)//2
                if nums[middle] == target:
                    return middle
                elif nums[middle] < target:
                    left = middle +1
                else:
                    right = middle -1
            return -1

        res = binarySearch(0, pivot-1)
        if res != -1:
            return res
        return binarySearch(pivot, len(nums)-1)