class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R = 0, len(numbers) - 1
        result = []
        while L < R:
            summed = numbers[L] + numbers[R]
            if summed > target:
                R -= 1
            elif summed < target:
                L += 1
            else:
                result.append(L + 1)
                result.append(R + 1)
                break
        return result

            