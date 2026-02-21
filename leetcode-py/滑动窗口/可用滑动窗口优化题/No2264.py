class Solution:
    # 暴力
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        for i in range(len(num)-2):
            # 字符串之间也可以比较
            if res < num[i] == num[i+1] == num[i+2]:
                res = num[i]
        return res * 3  # 3ms

class Solution:
    # 小滑
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        i = 0
        while i < len(num)-2:
            if num[i] == num[i+1]:
                if num[i] == num[i+2]:
                    if res < num[i]:
                        res = num[i]
                    i += 3
                else:
                    i += 2
            else:
                i += 1
        return res * 3  # 3ms

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        cnt = 1
        for i in range(1,len(num)):
            if num[i] != num[i-1]:
                cnt = 1
                continue
            cnt += 1
            if cnt == 3:
                res = max(num[i],res)
                cnt = 1
        return res * 3  # 3ms

class Solution:
    # leetcode 中无脑解法
    def largestGoodInteger(self, num: str) -> str:
        if "999" in num:
            return "999"
        if "888" in num:
            return "888"
        if "777" in num:
            return "777" 
        if "666" in num:
            return "666"
        if "555" in num:
            return "555"
        if "444" in num:
            return "444"
        if "333" in num:
            return "333"
        if "222" in num:
            return "222"
        if "111" in num:
            return "111"
        if "000" in num:
            return "000"
        return ""

R = ['999', '888', '777', '666', '555', '444', '333', '222', '111', '000']
class Solution:
    # leetcode 优雅无脑
    def largestGoodInteger(self, num: str) -> str:
        return next(filter(lambda r: r in num, R), '')
