class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        results = {}
        count = 1
        max_sequence = 1
        nums_set = set(nums)
        if len(nums) == 0:
            return 0
        for num in nums_set:
            if (num - 1) not in nums_set:
                start = num
                results[start] = 1
        
        for result in results:
            count = 1
            while True:
                if (result + count) in nums_set:
                    results[result] += 1
                    count += 1
                else:
                    count = 1
                    break
        for key,val in results.items():
            if val > max_sequence:
                max_sequence = val
        return max_sequence
        