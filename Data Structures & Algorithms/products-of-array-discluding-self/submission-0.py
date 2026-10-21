class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_side = []
        right_side = []
        result = []
        for count,num in enumerate(nums):
            if count == 0:
                left_side.append(1)
            else:
                next = nums[count - 1] * left_side[-1]
                left_side.append(next)
    

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_side.append(1)
            else:
                next = right_side[-1] * nums[i + 1]
                right_side.append(next)
        for i in range(len(nums)):
            result.append(left_side[i] * right_side[len(nums) - 1 - i])

        return result

        