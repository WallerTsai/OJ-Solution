from collections import Counter, defaultdict
from typing import List


class Solution:
    def score(self, cards: List[str], x: str) -> int:
        cnt0 = defaultdict(int)
        cnt1 = defaultdict(int)
        cnt2 = 0

        for s in cards:
            s0, s1 = s[0], s[1]
            if s0 == s1 == x:
                cnt2 += 1
                continue
            elif s0 == x:
                cnt0[s1] += 1
            elif s1 == x:
                cnt1[s0] += 1

        ans = 0

        temp = 0
        for i in cnt0.values():
            ans += min(temp, i)
            temp = abs(temp - i)

        if temp and cnt2:
            ans += min(temp, cnt2)
            cnt2 = max(cnt2 - temp, 0)

        temp = 0

        for i in cnt1.values():
            ans += min(temp, i)
            temp = abs(temp - i)

        if temp and cnt2:
            ans += min(temp, cnt2)

        return ans  # 错误
    

# 1. cnt = {ax:2, bx:2, cx:2} 可以形成 3 对， 而不是 2 对
#    pair 为 sum(cnt.value()) - max(cnt.value()) 和 sum(vnt.value()) // 2 的最小值
# 2. xx 是一个特列: 它不仅仅能跟剩下的未配对的cnt配对
#    还能通过拆散已配对的 pair 进行配对，可以使得 ans 增加
#    例： {ax:2, bx:2, xx:2} 最后答案是 pair + value(xx) // 2
# 3. xx 优先与剩余未配对的字符串配对，消耗 1 xx 增加 1 ans
#    最后才是通过拆散已经配对的字符串， 消耗 2 xx 增加 1 ans
class Solution:
    def score(self, cards: List[str], x: str) -> int:
        cnt0 = defaultdict(int)
        cnt1 = defaultdict(int)
        cnt2 = 0

        for s in cards:
            s0, s1 = s[0], s[1]
            if s0 == s1 == x:
                cnt2 += 1
                continue
            elif s0 == x:
                cnt0[s1] += 1
            elif s1 == x:
                cnt1[s0] += 1

        ans = 0

        sum0 = sum(cnt0.values())
        max0 = max(cnt0.values()) if cnt0 else 0
        pair0 = min(sum0 // 2, sum0 - max0)
        rem0 = sum0 - pair0 * 2
        if cnt2 and rem0:    
            ans += min(cnt2, rem0)
            cnt2 -= min(cnt2, rem0)


        sum1 = sum(cnt1.values())
        max1 = max(cnt1.values()) if cnt1 else 0
        pair1 = min(sum1 // 2, sum1 - max1)
        rem1 = sum1 - pair1 * 2
        if cnt2 and rem1:
            ans += min(cnt2, rem1)
            cnt2 -= min(cnt2, rem1)
        
        
        pair = pair1 + pair0
        ans += pair

        ans += min(cnt2 // 2, pair)

        return ans

class Solution:
    def score(self, cards: List[str], x: str) -> int:
        def cal(pcards):
            g_count = 0
            count = len(pcards)
            if pcards:
                card_count = Counter(pcards)
                g_count = min(count - max(card_count.values()), count // 2)
            return g_count, count - g_count * 2

        p0 = []
        p1 = []
        xx = x + x
        xx_count = 0
        for card in cards:
            if x in card:
                if card == xx:
                    xx_count += 1
                elif card[0] == x:
                    p0.append(card)
                elif card[1] == x:
                    p1.append(card)

        cp0, lp0 = cal(p0)
        cp1, lp1 = cal(p1)
        lcount = lp0 + lp1
        ret = cp0 + cp1
        if xx_count > 0:
            ret += min(xx_count, lcount)
            xx_count -= lcount
        if xx_count > 0:
            ret += min(cp0 + cp1, xx_count // 2)
        return ret

fun = Solution()
fun.score(["aa","aa","ab","aa","bb","ab"], 'a')