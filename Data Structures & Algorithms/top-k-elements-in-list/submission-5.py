class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bucket = []
        for i in range(len(nums) + 1):
            freq_bucket.append([])
        freq_map = {}
        result = []

        #create hash map
        for num in nums:
            freq_map[num] = 1 + freq_map.get(num, 0)
        
        for num, count in freq_map.items():
            freq_bucket[count].append(num)
    
        for i in range(len(freq_bucket) - 1 , 0 , -1):
            for num in freq_bucket[i]:
                result.append(num)
            if len(result) == k:
                    return result
