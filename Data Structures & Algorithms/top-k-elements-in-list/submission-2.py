class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            k_map[num] = 1 + k_map.get(num, 0)
        
        #build the bucket
        for num, count in k_map.items():
            bucket[count].append(num)
        
        #populate result
        for i in range(len(bucket) -1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        
