class Solution:
    def isValid(self, s: str) -> bool:
        strmap = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        strstack = []

        # if len(s) <= 1:
        #     return False

        for ltr in s:
            if ltr == "(" or ltr == "[" or ltr == "{":
                #append to stack
                strstack.append(ltr)
            else:
                if len(strstack) == 0:
                    return False
                elif strmap[ltr] == strstack[-1]:
                    strstack.pop()
                else:
                    return False
            
        return len(strstack) == 0
        

       