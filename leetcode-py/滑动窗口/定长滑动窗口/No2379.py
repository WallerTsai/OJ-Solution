class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = 0

        # 初始化
        for i in blocks[:k]:
            if i == 'W':
                res += 1

        count = res
        for j in range(k,len(blocks)):
            if blocks[j] == 'B' and blocks[j-k] == 'W':
                count -= 1
                if count < res:
                    res = count
            if blocks[j] == 'W' and blocks[j-k] == 'B':
                count += 1

        return res
    
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        res = sum(1 for i in range(k) if blocks[i] == "W")
        count = res
        for j in range(k,len(blocks)):
            if blocks[j] == 'B' and blocks[j-k] == 'W':
                count -= 1
                if count < res:
                    res = count
            if blocks[j] == 'W' and blocks[j-k] == 'B':
                count += 1

        return res
