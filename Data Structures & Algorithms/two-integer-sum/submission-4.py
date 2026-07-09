class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        value = 0
        # for i, num in range(len(nums)):
        #     if nums[i] in sumMap and (nums[i] * 2 == target):
        #         return [sumMap[nums[i]], i]
        #     else:
        #         sumMap[nums[i]] = i
        for i, num in enumerate(nums):
            value = target - num
            if value in sumMap:
                return [sumMap[value], i]
            sumMap[num] = i

            
        