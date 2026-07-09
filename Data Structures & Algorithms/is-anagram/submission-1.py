class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkerHash = {}
        if len(s) != len(t):
            return False
        for ltr in s:
            if ltr in checkerHash.keys():
                checkerHash[ltr] += 1
            else: 
                checkerHash[ltr] = 1
        
        for str in t:
            if str not in checkerHash.keys():
                return False
            else:
                checkerHash[str] -= 1
                if checkerHash[str] < 0:
                    return False
        return True

        