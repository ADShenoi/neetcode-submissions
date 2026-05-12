class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = ['(', '{', '[']
        close_brackets = [')', '}', ']']
        mp = {'(':')', '[':']', '{':'}'}

        stack = []

        for i in s:
            if i in open_brackets:
                stack.append(i)
            elif len(stack) == 0 and i in close_brackets:
                return False
            elif mp[stack[-1]] != i:
                return False
            else:
                stack.pop()
            
        
        return len(stack) == 0 