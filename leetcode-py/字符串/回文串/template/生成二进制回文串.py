from typing import List


def init() -> List[int]:
    MX = 5000

    # 哨兵，0 也是回文数
    palindromes = [0]
    pow2 = 1

    while True:
        # 生成奇数长度回文数
        for i in range(pow2, pow2 * 2):
            s = bin(i)[2:]
            x = int(s + s[::-1][1:], 2)
            if x > MX:
                return palindromes
            palindromes.append(x)

        # 生成偶数长度回文数
        for i in range(pow2, pow2 * 2):
            s = bin(i)[2:]
            x = int(s + s[::-1], 2)
            if x > MX:
                return palindromes
            palindromes.append(x)

        pow2 *= 2

palindromes = init()

