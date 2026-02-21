class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # 这道题不需要列出长度为k的二进制字符
        length = len(s)
        if length < 2 ** k : 
            return False
        res = set()
        for i in range(k,length+1):
            res.add(s[i-k:i])

        return True if len(res) == 2 ** k else False   # 244ms
    
    
        
fun = Solution()
outcome = fun.hasAllCodes("00110",2)
print(outcome)