from itertools import accumulate


class Solution:
    def is_k_palindrome(self, x: int, k: int) -> bool:
        digits = []
        while x:
            digits.append(x % k)
            x //= k
        return digits == digits[::-1]
    
    def kMirror(self, k: int, n: int) -> int:
        
        def generate_palindromes():

            base = 1
            while True:
                # 生成奇数长度回文数，例如 base = 10，生成的范围是 101 ~ 999
                for i in range(base, base * 10):
                    s = str(i)
                    x = int(s + s[::-1][1:])
                    yield x
                # 生成偶数长度回文数，例如 base = 10，生成的范围是 1001 ~ 9999
                for i in range(base, base * 10):
                    s = str(i)
                    x = int(s + s[::-1])
                    yield x
                
                base *= 10

        ans = 0
        cnt = 0

        for num in generate_palindromes():
            if self.is_k_palindrome(num,k):
                ans += num
                cnt += 1
                if cnt == n:
                    break
        return ans  # 2694
    

# 灵神
MAX_N = 30
ans = [[] for _ in range(10)]

# 力扣 9. 回文数
def is_k_palindrome(x: int, k: int) -> bool:
    if x % k == 0:
        return False
    rev = 0
    while rev < x // k:
        rev = rev * k + x % k
        x //= k
    return rev == x or rev == x // k

def do_palindrome(x: int) -> bool:
    done = True
    for k in range(2, 10):
        if len(ans[k]) < MAX_N and is_k_palindrome(x, k):
            ans[k].append(x)
        if len(ans[k]) < MAX_N:
            done = False
    if not done:
        return False
    for k in range(2, 10):
        ans[k] = list(accumulate(ans[k]))
    return True

def init() -> None:
    base = 1
    while True:
        # 生成奇数长度回文数，例如 base = 10，生成的范围是 101 ~ 999
        for i in range(base, base * 10):
            s = str(i)
            x = int(s + s[::-1][1:])
            if do_palindrome(x):
                return
        # 生成偶数长度回文数，例如 base = 10，生成的范围是 1001 ~ 9999
        for i in range(base, base * 10):
            s = str(i)
            x = int(s + s[::-1])
            if do_palindrome(x):
                return
        base *= 10
init()

class Solution:
    def kMirror(self, k: int, n: int) -> int:
        return ans[k][n - 1]