class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsmap = {}

        for num in nums:
            if num not in numsmap:
                numsmap[num] = 1
            else:
                return True
        return False
        