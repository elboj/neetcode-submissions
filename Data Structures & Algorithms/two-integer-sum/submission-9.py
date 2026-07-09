class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_hash = {}
        value = 0
        for index, num in enumerate(nums):
            value = target - num
            if value in index_hash:
                return [index_hash[value], index]
            index_hash[num] = index


        
            
        