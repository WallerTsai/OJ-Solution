class Solution:
    direction = [(0,1),(1,0),(0,-1),(-1,0)]
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0,0]
        di = 0
        cnt = 0
        for c in instructions:
            if c == 'G':
                pos[0] += self.direction[di][0]
                pos[1] += self.direction[di][1]
            if c == 'R':
                di = (di + 1) % 4
                cnt += 1
            if c == 'L':
                di = (di - 1) % 4
                cnt -= 1
        if pos == [0,0] or cnt%4 :
            # 循环条件1:一次循环就在原点
            # 循环条件2：左右方向改变,改变四次则归0
            return True
        else:
            return False