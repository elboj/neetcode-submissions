class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      index_map = {}
      key = 0
      for count,num in enumerate(nums):
        key = target - num
        if key in index_map:
            return [index_map[key], count]
        index_map[num] = count

        

        
            
        