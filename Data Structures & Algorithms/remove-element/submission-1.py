class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        newlist = []
        for num in nums:
            if num != val:
                newlist.append(num)
        for i in range(len(newlist)):
            nums[i] = newlist[i]
        return len(newlist)