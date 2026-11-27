class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        startNumbers = []
        numsMap = {}
    
        maxValue = 0

    #add starting numbers to array
        for num in numSet:
            if (num - 1) not in numSet:
                startNumbers.append(num)
                numsMap[num] = 1
        
        for num in startNumbers:
            count = 1
            while True:
                if (num + count) in numSet:
                    numsMap[num] += 1
                    count += 1
                else:
                    # count = 1
                    break
        for key,val in numsMap.items():
            if val > maxValue:
                maxValue = val
        return maxValue
       