# https://leetcode.com/problems/valid-parentheses/description/
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close = {')':'(','}':'{',']':'['}
        for i in s:
            if stack and i in close and stack[-1] == close[i]: stack.pop()
            elif i in close: return False
            else: stack.append(i)
        if stack: return False
        else: return True