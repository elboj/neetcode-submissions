class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        holder_value = 0
        for count,num in enumerate(nums):
            if count == 0:
                result.append(1)
            else:
                next = nums[count - 1] * result[-1]
                result.append(next)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                holder_value = 1
            else:
                holder_value = holder_value * nums[i + 1]
                result[i] = result[i] * holder_value
    
        return result

        