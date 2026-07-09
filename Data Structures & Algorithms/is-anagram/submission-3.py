class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_hash = {}
        t_hash = {}

        for ltr in s:
            s_hash[ltr] = s_hash.get(ltr, 0) + 1
        
        for ltr in t:
            t_hash[ltr] = t_hash.get(ltr, 0) + 1
        #Basically I built two hash map and compared if they are same
        return s_hash == t_hash
        

        