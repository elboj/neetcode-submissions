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
                #deals with cases where there's no opening bracket in string
                if len(strstack) == 0:
                    return False
                #Handles the popping of stack
                elif strmap[ltr] == strstack[-1]:
                    strstack.pop()
                #Handles cases where close doesnt equal open
                else:
                    return False
        #Will always be true for correct scenarios
        return len(strstack) == 0
        

       