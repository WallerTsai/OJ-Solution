
# class Solution:
#     def longestPalindrome(self, s: str) -> str:
#         i = 0
#         lenth=len(s)
#         max_index = None
#         max_num = 0
#         else_index = None
#         while i != lenth:
#             addition = True
#             right = 0
#             while i-right-1>=0 and i+right+1 <= lenth-1:
                    
#                     if s[i] != s[i+right+1]:
#                         addition = False

#                     if s[i-right-1] == s [i+right+1]:
#                         right += 1
#                     else:
#                         break

#             if i+right+1<len(s) and s[i] == s[i+right+1] and addition:
#                 else_index = i

#             if right > max_num:
#                 if addition:
#                     else_index = i
#                 max_num = right
#                 max_index = i
#             i += 1
#         if max_index and max_index != else_index:
#             return s[max_index-max_num:max_index+max_num+1]
#         elif else_index is not None :
#             return s[else_index-max_num:else_index+max_num+2]
#         else:
#             return s[0]
#         ### wrong
        
# 动态规划
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_lenth = 1

        if n < 2:
            return s

        begin_index = 1
        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = True

        # lenth 为回文数的长度,从2开始到n
        for lenth in range(2,n+1):
            # i为左下标
            for i in range(n):
                # j为右下标
                j = lenth + i - 1

                if j >= n:
                    break

                if s[i] == s[j]:
                    if j-i <= 2:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i+1][j-1]
                else:
                    pass
                if dp[i][j] == True and lenth > max_lenth:
                    begin_index = i
                    max_lenth = lenth
        return s[begin_index:begin_index+max_lenth]


if __name__ == "__main__":
    # s1 = "babad"
    # s2 = "cbbd"
    # s3 = "aaaa" #报错
    # fun = Solution()
    # outcome = fun.longestPalindrome(s1)
    # print(outcome)
    n = 5
    dp = [[False] * n for _ in range(n)]
    print(dp)


# 2026年3月20日
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        k = 0
        left = 0

        for i in range(2 * n - 1):
            l, r  = i // 2, (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > k:
                k = r - l - 1
                left = l + 1
        return s[left: left + k]