class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        li = [float(poured)]
        for i in range(1, query_row + 1):
            nxt = [float(0)] * (i + 1)
            for j, x in enumerate(li):
                if x > 1:
                    half = (x - 1) / 2
                    nxt[j] += half
                    nxt[j + 1] += half
            li = nxt
        return min(li[query_glass], float(1))