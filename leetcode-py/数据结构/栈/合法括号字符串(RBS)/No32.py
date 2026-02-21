# class Solution:
#     def longestValidParentheses(self, s: str) -> int:

#         length = len(s)

#         if length < 2:
#             return 0

#         effective_rigth = []
#         left_num = 0
#         for i in range(length):
#             if s[i] == "(":
#                 left_num += 1
#             if left_num > 0 and s[i] == ")":
#                 left_num -= 1
#                 effective_rigth.append(i)

#         if len(effective_rigth) < 2:
#             return len(effective_rigth) * 2

#         lengths = []
#         temp_length = 1
#         for j in range(len(effective_rigth)):
#             if j < len(effective_rigth)-1:
#                 if effective_rigth[j]+1 == effective_rigth[j+1] or effective_rigth[j]+2 == effective_rigth[j+1]:
#                     temp_length += 1
#                 else:
#                     lengths.append(temp_length)
#                     temp_length = 1
#             else:
#                 lengths.append(temp_length)

#         return max(lengths)*2   #逻辑错误
                
class Solution:
    def longestValidParentheses(self, s: str) -> int:

        length = len(s)

        if length < 2:
            return 0

        target_list = ["."] * length
        left_list = []
        for i in range(length):
            if s[i] == "(":
                left_list.append(i)
            if s[i] == ")" and len(left_list) != 0:
                target_list[i] = ")"
                target_list[left_list[-1]] = "("
                left_list.pop()

        out_list = "".join(target_list).split(".")
        return max(len(item) for item in out_list)
    

class Solution:
    # 作者：郁郁雨
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        for i in range(len(s)):
            if not stack or s[i] == '(' or s[stack[-1]] == ')':
                stack.append(i)
            else:
                stack.pop()
                res = max(res, i - (stack[-1] if stack else - 1))
        return res



# 2026年2月20日
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        ans = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif len(stack) > 1:
                stack.pop()
                ans = max(ans, i - stack[-1])
            else:
                stack[-1] = i
        return ans
