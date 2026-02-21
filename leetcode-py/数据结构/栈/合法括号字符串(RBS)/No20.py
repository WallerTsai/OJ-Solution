# class Solution:
#     def isValid(self, s: str) -> bool:
#         validmap = {
#             ")": "(",
#             "]": "[",
#             "}": "{"
#         }
#         stack = []
#         for i in s:
#             if i in validmap.values():
#                 stack.append(i)
#             else:
#                 try:
#                     if stack[-1] == validmap[i]:
#                         stack.pop(-1)
#                     else:
#                         return False
#                 except:
#                     return False
#         # return True if stack is None else False #空列表不为None
#         return True if not stack else False

# class Solution:
#     # 作者：Krahets
#     def isValid(self, s: str) -> bool:
#         dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
#         stack = ['?']
#         for c in s:
#             if c in dic: stack.append(c)
#             elif dic[stack.pop()] != c: return False 
#         return len(stack) == 1

class Solution:
    # 极简
    def isValid(self, s: str) -> bool:
        dict = {'(':')','{':'}','[':']'}
        stack = []
        for c in s:
            if c in dict:
                stack.append(dict[c])
            else:
                if len(stack)== 0 or c!=stack.pop():
                    return False
        return len(stack) == 0

if __name__ == "__main__":
    fun = Solution()
    s = "()"
    print(fun.isValid(s))