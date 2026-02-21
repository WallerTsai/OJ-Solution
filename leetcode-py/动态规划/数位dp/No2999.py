class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        num = int(s)
        length = len(s)
        if num > finish:
            return 0
        
        def fit(s:str, limit:int) -> str:
            s = list(map(int,s))
            i = 0
            ans = []
            for c in s[::-1]:
                c += i
                if c > limit:
                    ans.append(0)
                    i = 1
                else:
                    ans.append(c)
                    i = 0
            if i > 0:
                ans.append(i)
            return "".join(map(str,ans[::-1]))


        if num < start:
            if len(str(start)) > length:
                pre = str(start)[:len(str(start)) - len(s)]
                s = fit(pre,limit) + s
            else:
                s = "1" + s
        
        finish_length = len(str(finish))
        s = "0" * (finish_length - len(s)) + s


        ans = 0

        # 首位特殊处理
        for i in range(int(s[0]),limit+1):
            n = int(str(i) + s[1:])
            if n <= finish:
                ans += 1

        for i in range(1,len(s) - length):
            ans *= limit - int(s[i]) + 1

        return ans  # 错误，不能枚举
     


fun = Solution()
fun.numberOfPowerfulInt(1,6000,4,"124")