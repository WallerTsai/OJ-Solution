class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        pre = directions[0]
        for ch in directions:
            if ch == 'S'and pre == 'R':
                    ans += 1
                    pre = 'S'
            elif ch == 'L' and pre != 'L':
                if pre == 'R':
                    ans += 2
                elif pre == 'S':
                    ans += 1
                pre = 'S'
            else:
                pre = ch
        return ans  # 错误
    
class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        have_s = False
        pre_right = 0
        pre = directions[0]
        for ch in directions:
            if ch == 'L':
                if not have_s:
                    continue
                if pre == 'R':
                    ans += 2
                    ans += pre_right - 1
                    pre_right = 0
                    pre = 'S'
                    have_s = True
                else:
                    ans += 1
            elif ch == 'S':
                ans += pre_right
                pre_right = 0
                pre = 'S'
                have_s = True
            else:
                pre_right += 1
                pre = 'R'
                have_s = True

        return ans  # 107ms

class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        flag = -1

        for ch in directions:
            if ch == 'L':
                if flag >= 0:
                    ans += flag + 1
                    flag = 0
            elif ch == 'S':
                if flag > 0:
                    ans += flag
                flag = 0
            else:
                if flag >= 0:
                    flag += 1
                else:
                    flag = 1

        return ans  # 99ms
    

class Solution:
    # 灵神
    def countCollisions(self, s: str) -> int:
        s = s.lstrip('L')  # 前缀向左的车不会发生碰撞
        s = s.rstrip('R')  # 后缀向右的车不会发生碰撞
        return len(s) - s.count('S')  # 剩下非停止的车必然会碰撞    # 4ms