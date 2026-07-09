class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newNums  = []
        for num in nums:
            newNums.append(num)
        return newNums + nums
        