class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        li = []
        count = start = 0
        for i, ch in enumerate(s):
            if ch == '(':
                count += 1
            else:
                count -= 1
                if count == 0:
                    li.append(s[start + 1: i])
                    start = i + 1
        return ''.join(li) 
            