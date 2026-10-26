class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers) - 1
        while L < R:
            LRSum = numbers[L] + numbers[R]
            if LRSum  == target:
                return [L+1 , R+1]
            elif LRSum  > target:
                R -= 1
                continue
            elif LRSum  < target:
                L += 1
                continue
            