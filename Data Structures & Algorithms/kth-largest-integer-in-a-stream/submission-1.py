class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kelement = k
        self.newnums = nums.copy()

    def add(self, val: int) -> int:
        self.newnums.append(val)
        self.newnums.sort()
        return self.newnums[len(self.newnums)-self.kelement]
