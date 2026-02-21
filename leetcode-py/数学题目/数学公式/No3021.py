class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        ans = 0
        even = m // 2
        odd = m - even
        
        for i in range(1, n + 1):
            if i % 2:
                ans += even
            else:
                ans += odd

        return ans
    
class Solution:
    # 灵神
    # https://leetcode.cn/problems/alice-and-bob-playing-flower-game/solutions/2622659/o1-gong-shi-yi-xing-dai-ma-pythonjavacgo-f7ch/?envType=daily-question&envId=2025-08-29
    def flowerGame(self, n: int, m: int) -> int:
        return n * m // 2