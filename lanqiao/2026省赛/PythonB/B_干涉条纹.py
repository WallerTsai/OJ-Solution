import math

def main():
    MOD = 998244353

    A = 20269876543210
    B = 20260123456789
    total = A + B

    sqrt_total = math.isqrt(total)
    ans = 0

    for s in range(sqrt_total + 1):
        pow2 = s * s
        
        L = max(0, pow2 - B)
        R = min(A, pow2)

        if R >= L:
            ans += (R - L + 1)
            ans %= MOD

    print(ans % MOD)

if __name__ == "__main__":
    main()

# gemini
def solve():
    A = 20269876543210
    B = 20260123456789
    MOD = 998244353
    
    # 辅助函数：计算 0 到 n 的平方和
    def sum_sq(n):
        if n <= 0: return 0
        return n * (n + 1) * (2 * n + 1) // 6

    # 确定三个阶段的 k 的边界
    # math.isqrt 可以直接对大整数开平方并向下取整 (Python 3.8+)
    K1 = math.isqrt(B)
    K2 = math.isqrt(A)
    Kmax = math.isqrt(A + B)
    
    # 阶段 1：k 从 0 到 K1
    # sum(k^2 + 1) = sum_sq(K1) + (K1 + 1)
    part1 = sum_sq(K1) + (K1 + 1)
    
    # 阶段 2：k 从 K1 + 1 到 K2
    # sum(B + 1) = 个数 * (B + 1)
    part2 = (K2 - K1) * (B + 1)
    
    # 阶段 3：k 从 K2 + 1 到 Kmax
    # sum(A + B + 1 - k^2)
    count3 = Kmax - K2
    part3 = count3 * (A + B + 1) - (sum_sq(Kmax) - sum_sq(K2))
    
    # 总计并取模
    total = part1 + part2 + part3
    ans = total % MOD
    
    print(ans)

if __name__ == '__main__':
    solve()