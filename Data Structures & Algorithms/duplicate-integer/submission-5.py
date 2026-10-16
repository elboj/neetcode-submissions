class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False
        # num_map = {}
        # for num in nums:
        #     if num in num_map:
        #         return True
        #     num_map[num] = 1
        # return False

        