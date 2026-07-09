class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {}
        value = 0
        for i in range(len(nums)):
            if nums[i] in sumMap and (nums[i] * 2 == target):
                return [sumMap[nums[i]], i]
            else:
                sumMap[nums[i]] = i
        for num in nums:
            if num * 2 != target:
                value = target - num
                if value in sumMap:
                    return [sumMap[num], sumMap[value]]

            
        