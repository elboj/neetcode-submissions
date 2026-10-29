class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        #create fixed value
        for i in range(len(nums) - 2):
            #check duplicate
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            num = nums[i]
            L,R = i + 1, len(nums) - 1
            while L < R:
                total = num + nums[L] + nums[R]
                if total == 0:
                    result.append([num, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
    
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                elif total < 0:
                    L += 1
                else:
                    R -= 1
        return result
        