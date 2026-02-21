from typing import List


class Solution:
    # 不妨假设每次滑动都和每段的右边贴合
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort(key=lambda x:x[0])
        res = cover = left = 0
        for zone in tiles:
            cover += zone[1] - zone[0] + 1

            while tiles[left][1] < zone[1] - carpetLen + 1:
                cover -= tiles[left][1] - tiles[left][0] + 1
                left += 1
            # 如果左段在某一块的内部
            uncover = max(zone[1]-carpetLen+1-tiles[left][0],0)
            res = max(res,cover-uncover)
        return res  # 119ms

class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # 每次覆盖时都应选择一个tile的左边界，这样能保证覆盖的瓷砖最多
        # l，r分别表示能到达的左瓷砖和右瓷砖，那么必定是递增的，因为循环到下一个瓷砖时，右瓷砖一定变大
        # 要排个序
        tiles.sort(key = lambda x:x[0])
        l = 0
        r = 0
        
        # 此时需要记录两个瓷砖之间的空白瓷砖数，再用carpetLen减去即为覆盖的长度
        res = 0
        n = len(tiles)
        fg = 0
        while l < n and r < n:
            # r表示当前要覆盖的白块
            if tiles[r][1] - tiles[l][0] + 1 <= carpetLen:
                # 右边界砖块的右区间与左边界砖块的左区间是否超过了毯子的长度
                ## 没超过
                ## 那么右边界的区间范围被全部囊括，也就是覆盖完毕
                fg += tiles[r][1] - tiles[r][0] + 1
                r += 1
            else:
                # 超过了毯子的长度，那么毯子也就只能从左边界的左区间到右边界的右区间为止
                # 那么具体覆盖了多少个呢？
                # 之前都已经记录过了，因此此时查看能覆盖当前区间的情况（因为当前区间覆盖不完）
                res = max(res,fg + max(tiles[l][0] + carpetLen - tiles[r][0],0))

                # 减去左边界的砖块数量，并移动左边界
                fg -= (tiles[l][1] - tiles[l][0] + 1)
                l += 1
        res = max(res,fg)
        return res


