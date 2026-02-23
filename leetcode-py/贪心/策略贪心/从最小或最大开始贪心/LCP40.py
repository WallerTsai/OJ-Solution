from typing import List
# class Solution:
#     def maximumScore(self, cards: List[int], cnt: int) -> int:
#         # cards.sort(reverse=True)
#         res = 0
#         even = [ x for x in cards if x % 2 == 0]
#         odd = [ x for x in cards if x % 2 != 0]
#         even.sort()
#         odd.sort()
#         while cnt:
#             if not even:
#                 for _ in range(min(cnt,len(even))):
#                     res += odd.pop()
#                 break
#             if not odd:
#                 for _ in range(min(cnt,len(even))):
#                     res += even.pop()
#                 break
#             if len(odd) == 1:
#                 odd.pop()
#                 continue
#             if even[-1] > odd[-1]:
#                 res += even.pop()
#                 cnt -= 1
#             else:
#                 if cnt < 2:
#                     res += even.pop()
#                     break
#                 if len(even) == 1:
#                     for _ in range(2):
#                         res += odd.pop()
#                     cnt -= 2
#                     continue
#                 if even[-1] + even[-2] <= odd[-1] + odd[-2]:
#                     for _ in range(2):
#                         res += odd.pop()
#                 else:
#                     for _ in range(2):
#                         res += even.pop()
#                 cnt -= 2

#         if res % 2 == 0:
#             return res
#         else:
#             return 0
#     # 暴力大错

# class Solution:
#     def maximumScore(self, cards: List[int], cnt: int) -> int:
#         cards.sort(reverse=True)
#         # 先贪心的取cnt个最大数
#         res = sum(cards[:cnt])
#         # 如果结果为偶直接输出即可
#         if res % 2 == 0:
#             return res
#         # 长度相等且res不是偶数，则直接截断
#         if len(cards) == cnt:
#             return 0
        
#         even = -1
#         for i in cards[cnt:]:
#             if i % 2 == 0:
#                 even = i
#                 break

#         if even != -1:
#             for card in cards[cnt-1::-1]:
#                 if card % 2 != 0:
#                     res -= card
#                     res += even
#                     break
#         else:
#             odd = -1
#             for i in cards[cnt:]:
#                 if i % 2 != 0:
#                     odd = i
#                     break
#             if odd != -1:
#                 for card in cards[cnt-1::-1]:
#                     if card % 2 == 0:
#                         res -= card
#                         res += odd
#                         break

#         return res if res % 2 == 0 else 0
#     # 最后个测试卡了
#     # cards = [9,5,9,1,6,10,3,4,5,1]
#     # cnt = 2
#     # res = 16
#     # ans = 18

class Solution:
    def maximumScore(self, cards: List[int], cnt: int) -> int:
        cards.sort(reverse=True)
        s = sum(cards[:cnt])  # 最大的 cnt 个数之和
        if s % 2 == 0:  # s 是偶数
            return s

        def replaced_sum(x: int) -> int:
            for v in cards[cnt:]:
                if v % 2 != x % 2:  # 找到一个最大的奇偶性和 x 不同的数
                    return s - x + v  # 用 v 替换 s
            return 0

        ## 下面这很巧妙
        x = cards[cnt - 1]
        ans = replaced_sum(x)  # 替换 x
        for v in cards[cnt - 1::-1]:
            if v % 2 != x % 2:  # 找到一个最小的奇偶性和 x 不同的数
                ans = max(ans, replaced_sum(v))  # 替换
                break
        return ans

# 作者：灵茶山艾府
# 链接：https://leetcode.cn/problems/uOAnQW/solutions/991699/pai-xu-tan-xin-by-endlesscheng-wgk7/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
