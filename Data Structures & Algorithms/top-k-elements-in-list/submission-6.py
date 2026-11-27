class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = []
        numsMap = {}
        result = []

        #create bucket
        for i in range(len(nums) + 1):
            bucket.append([])
        
        #create hashmap
        for num in nums:
            numsMap[num] = numsMap.get(num, 0) + 1

        #fill bucket
        for key, value in numsMap.items():
            bucket[value].append(key)

        #get top most
        for i in range(len(bucket) - 1, 0 , -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
