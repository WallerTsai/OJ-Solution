from typing import List


class Robot:
    "一个只走外圈的机器人"
    direction = (1,0),(0,1),(-1,0),(0,-1)
    dir_name = ("East","North","West","South")
    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.width = width
        self.height = height
        self.di = 0

    def step(self, num: int) -> None:
        while num:
            nx = self.x + self.direction[self.di][0]
            ny = self.y + self.direction[self.di][1]
            if not (0 <= nx < self.width) or not (0 <= ny <self.height):
                self.di = (self.di + 1) % 4
                continue
            self.x = nx
            self.y = ny
            num -= 1

    def getPos(self) -> List[int]:
        return [self.x,self.y]

    def getDir(self) -> str:
        return self.dir_name[self.di]

    # 超时

    # 把他拉成直线
class Robot:
    # 灵神
    def __init__(self, width: int, height: int):
        self.w, self.h, self.s = width, height, 0

    def step(self, num: int) -> None:
        # 由于机器人只能走外圈，那么走 (w+h-2)*2 步后会回到起点
        # 同时，将 s 取模固定在 [1,(w+h-2)*2] 范围内，这样不需要特判处于原点时的方向
        self.s = (self.s + num - 1) % ((self.w + self.h - 2) * 2) + 1

    def get(self):
        s, w, h = self.s, self.w, self.h
        if s < w: return s, 0, "East"
        if s < w + h - 1: return w - 1, s - w + 1, "North"
        if s < w * 2 + h - 2: return w * 2 + h - 3 - s, h - 1, "West"
        return 0, (w + h - 2) * 2 - s, "South"

    def getPos(self) -> List[int]:
        x, y, _ = self.get()
        return [x, y]

    def getDir(self) -> str:
        return self.get()[2]    # 78ms
    
class Robot:

    def __init__(self, width: int, height: int):
        self.w=width
        self.h=height
        self.L=(width+height-2)*2
        self.cur_d=0
        self.initial=True

    def step(self, num: int) -> None:
        if num>0:
            self.initial=False
        self.cur_d=(self.cur_d+num)%self.L


    def getPos(self) -> List[int]:
        d=self.cur_d
        if self.cur_d<self.w:
            return [self.cur_d,0]
        d-=(self.w-1)
        if d<self.h:
            return [self.w-1,d]
        d-=(self.h-1)
        if d<self.w:
            return [self.w-1-d,self.h-1]
        d-=(self.w-1)
        return [0,self.h-1-d]

    def getDir(self) -> str:
        d=self.cur_d
        if d==0:
            return "East" if self.initial else "South"
        if d<self.w:
            return "East"
        d-=(self.w-1)
        if d<self.h:
            return "North"
        d-=(self.h-1)
        if d<self.w:
            return "West"
        d-=(self.w-1)
        return "South"