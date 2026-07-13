class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
       count = reset = 0
       for num in nums:
        if num == 1:
            count += 1
        else:
            count = 0
        reset = max(count, reset)
       return reset 