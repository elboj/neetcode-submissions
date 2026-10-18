class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}
        final_array = []
        k_frequency = []
        for num in nums:
            if num in k_map:
                k_map[num] += 1
            else:
                k_map[num] = 1

        for key in k_map:
            final_array.append([k_map[key], key])
        
        sorted_array = sorted(final_array, reverse=True)
        
        for x in sorted_array[:k]:
            k_frequency.append(x[1])
        return k_frequency

        