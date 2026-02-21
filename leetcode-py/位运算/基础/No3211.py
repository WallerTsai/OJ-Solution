from typing import List

class Solution:
    # 小妙
    # 递归
    def validStrings(self, n: int) -> List[str]:
        res = []
        path = [""] * n

        def dfs(i:int):
            if i == n:
                res.append(''.join(path))
                return
            
            path[i] = '1'
            dfs(i+1)

            if i == 0 or path[i-1] == '1':
                path[i] = '0'
                dfs(i+1)
        
        dfs(0)
        return res
    

class Solution:
    # 动态规划
    # leetcode 最快
    def validStrings(self, n: int) -> List[str]:
        ans=["0","1"]
        for _ in range(1,n):
            temp=[]
            for j in range(len(ans)):
                if ans[j][-1]=="0":
                    temp.append(ans[j]+"1")
                else:
                    temp.append(ans[j]+"0")
                    temp.append(ans[j]+"1")
            ans=temp
        return ans
    

# 如果这个二进制没有相邻的 0，则代表是一个有效字符串。
# 那么怎么判断是否有相邻的 0 呢？首先将数字按位取反，记为 t。
# 如果 t & (t>>1) 为 0，则 t 中没有相邻的 0

# 题目要求找出不能连续出现两个 0，这时可运用“正难则反”的思路。
# 我们不妨反过来思考连续两个 1 的规律。
# 例如，有数字序列为 1011，其中存在连续两个 1。
# 可以看到，连续两个 1 右移一位后进行自身相与，结果不为 0。
# 只要结果不为 0，就表明有连续两个 
# 1 进行右移操作，会与前面一个 1 进行相与操作，两个 1 相与的结果必然不为 0。
# 如此，通过判断结果是否为 0，就能确定是否存在连续两个 1。
class Solution:
    # 位运算
    def validStrings(self, n: int) -> List[str]:
        res = []
        # 掩码
        mask = (1 << n) -1
        for i in range(1<<n):   # 1<<n 也就是2**n
            t = mask ^ i
            if not (t & t>>1):
                res.append(f"{i:0{n}b}") # f-string 格式化: 0：用0填充 {n}：一共n位 b：二进制形式
        return res


