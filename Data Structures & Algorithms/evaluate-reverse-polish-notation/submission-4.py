class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            newlist = []
            for token in tokens:
                if token == "+":
                    right = newlist.pop()
                    left = newlist.pop()
                    newlist.append(left + right)
                    # newlist[:] = newlist[-1:]
                elif token == "*":
                    right = newlist.pop()
                    left = newlist.pop()
                    newlist.append(left * right)
                elif token == "-":
                    right = newlist.pop()
                    left = newlist.pop()
                    newlist.append(left - right)
                elif token == "/":
                    right = newlist.pop()
                    left = newlist.pop()
                    newlist.append(int(left / right))
                else:
                    newlist.append(int(token))
            return newlist[0]
                