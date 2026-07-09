class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        newlist = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
            else:
                newlist = arr[i+1:]
                k = 0
                for num in newlist:
                    if num > k:
                        k = num
                arr[i] = k
        return(arr)

        