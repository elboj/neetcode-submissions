class Solution:
    def isPalindrome(self, s: str) -> bool:
         #remove all white spaces in character
        cleaned_text = "".join(char for char in s if char.isalnum()).lower()

        #set our pointers beginning and end of string
        L,R = 0, len(cleaned_text) - 1

        #set while loop for intersection point... while L < R
        while L < R:
            if cleaned_text[L] != cleaned_text[R]:
                return False
            L += 1
            R -= 1  
        return True
        