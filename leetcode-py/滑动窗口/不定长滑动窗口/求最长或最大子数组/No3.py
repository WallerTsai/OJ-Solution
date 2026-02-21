

#审题不仔细
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         times = 0
#         list_1 = []
#         for i in s:
#             if i in list_1:
#                 break
#             else:
#                 list_1.append(i)
#                 times += 1
#         return times

# if __name__ == '__main__':
#     str = "abcabcbb"
#     a =Solution()
#     eg1 = a.lengthOfLongestSubstring(s=str)
#     print(eg1)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         temt = 0
#         max_times = 0
#         list_1 = []
#         for i in s:
#             if i in list_1:
#                 if temt > max_times:
#                     max_times = temt
#                 temt = 1
#             else:
#                 list_1.append(i)
#                 temt += 1
#         return max_times

# if __name__ == '__main__':
#     s1 = "abcabcbb"
#     s2 = "pwwkew"
#     error_s = " " #应该输出1
#     a =Solution()
#     eg1 = a.lengthOfLongestSubstring(error_s)
#     print(eg1)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         temt = 0
#         max_times = 0
#         list_1 = []
#         for i in s:
#             if i in list_1:
#                 temt = 1
#             else:
#                 list_1.append(i)
#                 temt += 1
#             if temt > max_times:
#                 max_times = temt
#         return max_times

# if __name__ == '__main__':
#     s1 = "abcabcbb"
#     s2 = "pwwkew"
#     error_s = "dvdf" #应该输出3
#     #代码根本上逻辑错误
#     a =Solution()
#     eg1 = a.lengthOfLongestSubstring(error_s)
#     print(eg1)

# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         temt = 0
#         max_times = 0
#         list_1 = []
#         for i in s:
#             if i in list_1:
#                 location = list_1.index(i)
#                 list_1 = list_1[location:]
#                 temt = len(list_1)
#             else:
#                 list_1.append(i)
#                 temt += 1
#             if temt > max_times:
#                 max_times = temt
#         return max_times

# if __name__ == '__main__':
#     s1 = "abcabcbb"
#     s2 = "pwwkew"
#     s3 = " "
#     s4 = "dvdf" 
#     error_s = "aabaab!bb"
#     a =Solution()
#     eg1 = a.lengthOfLongestSubstring(error_s)
#     print(eg1)

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temt = 0
        max_times = 0
        list_1 = []
        for i in s:
            if i in list_1:
                location = list_1.index(i)
                list_1.append(i)
                list_1 = list_1[location+1:]
                temt = len(list_1)
            else:
                list_1.append(i)
                temt += 1
            if temt > max_times:
                max_times = temt
        return max_times

# 2024.12.26 以下
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        aset = set()

        for c in s:
            while c in aset:
                aset.remove(s[left])
                left += 1
            aset.add(c)
            res = max(res,len(aset))
        return res  # 19ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        aset = set()

        for right,c in enumerate(s):
            while c in aset:
                aset.remove(s[left])
                left += 1
            aset.add(c)
            res = max(res,right-left+1)
        return res  # 19ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = left = 0
        cnt = defaultdict(int)

        for right,c in enumerate(s):
            cnt[c] += 1
            while cnt[c] > 1:
                cnt[s[left]] -= 1
                left += 1
            if res < right-left+1:
                res = right-left+1
        return res  # 17ms


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "pwwkew"
    s3 = " "
    s4 = "dvdf" 
    s5 = "aabaab!bb"
    a =Solution()
    eg1 = a.lengthOfLongestSubstring(s5)
    print(eg1)
