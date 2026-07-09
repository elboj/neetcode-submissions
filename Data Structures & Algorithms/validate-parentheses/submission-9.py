class Solution:
    def isValid(self, s: str) -> bool:
        strmap = {
            "]":"[",
            "}":"{",
            ")":"("
        }

        strstack = []

        for char in s:
            if  char == "[" or char == "(" or char == "{":
                strstack.append(char)
            else:
                if len(strstack) == 0:
                    return False
                if strmap[char] != strstack[-1]:
                    return False
                strstack.pop()
        return len(strstack) == 0