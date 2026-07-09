class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsmap = set()

        for num in nums:
            if num in numsmap:
                return True
            numsmap.add(num)
        return False

        # for num in nums:
        #     if num not in numsmap:
        #         numsmap[num] = 1
        #     else:
        #         return True
        # return False
        