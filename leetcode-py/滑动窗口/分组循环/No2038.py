class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        cnt_a = cnt_b = i = 0
        n = len(colors)

        while i < n:
            start = i
            i += 1
            while i < n and colors[i] == colors[i - 1]:
                i += 1
            if colors[start] == 'A':
                cnt_a += max(0, i - start - 2)
            else:
                cnt_b += max(0, i - start - 2)
        
        return cnt_a > cnt_b


