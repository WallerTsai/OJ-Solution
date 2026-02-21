from typing import List
from bisect import bisect_right

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        length = len(potions)
        potions.sort()
        for spell in spells:
            index = bisect_right(potions,(success-1)//spell)    # 思考这里的success为什么要减1
            res.append(length-index)
        return res

# max∗x>=success =>
# x>=⌊(success+max−1)/max⌋ =>
# x>=⌊(success−1)/max⌋+1
# 可知 x>⌊(success−1)/max⌋，即 x 至少要大于 minPotion=⌊(success−1)/max⌋。

class Solution:
    # 二分 + 前缀和
    # leetcode大佬
    # 想出这个绝对是个天才
    def successfulPairs(self, spells, potions, success):
        max_spell = max(spells)
        min_potion = (success - 1) // max_spell
        count = [0] * (max_spell + 1)
        
        for potion in potions:
            if potion > min_potion:
                count[(success + potion - 1) // potion] += 1
        
        for i in range(1, max_spell + 1):
            count[i] += count[i - 1]
        
        result = []
        
        for spell in spells:
            result.append(count[spell])
        
        return result
    
class Solution:
    # 灵神
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        mx = max(potions)
        cnt = [0] * (mx + 1)
        for y in potions:
            cnt[y] += 1  # 统计每种药水的出现次数

        # 计算 cnt 的后缀和
        for i in range(mx - 1, -1, -1):
            cnt[i] += cnt[i + 1]
        # 计算完毕后，cnt[i] 就是 potions 值 >= i 的药水个数

        for i, x in enumerate(spells):
            low = (success - 1) // x + 1
            spells[i] = cnt[low] if low <= mx else 0
        return spells