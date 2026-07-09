class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        checkerHash = {}
        if len(s) != len(t):
            return False

        # for ltr in s:
        #     if ltr in checkerHash:
        #         checkerHash[ltr] += 1
        #     else: 
        #         checkerHash[ltr] = 1
        #below is cleaner
        for i, ltr in enumerate(s):
            checkerHash[s[i]] = 1 + checkerHash.get(s[i], 0)
        
        for str in t:
            if str not in checkerHash:
                return False
            else:
                checkerHash[str] -= 1
                if checkerHash[str] < 0:
                    return False
        return True

        