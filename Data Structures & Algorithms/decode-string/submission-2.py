class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch == ']':
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()
                count = ''
                while stack and stack[-1].isdigit():
                    count = stack.pop() + count
                count = int(count)
                string = string * count
                stack.append(string)
            else:
                stack.append(ch)
        return ''.join(stack)