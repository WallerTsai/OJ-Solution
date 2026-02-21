class Solution:
    # 模拟
    def kthCharacter(self, k: int) -> str:
        words = [0]
        while len(words) < k:
            words.extend([(x + 1) % 26 for x in words])
        return chr(ord("a") + words[k - 1]) # 3ms
    

class Solution:
# 作者：wxyz
# 链接：https://leetcode.cn/problems/find-the-k-th-character-in-string-game-i/solutions/3714065/san-jie-mo-ni-er-jin-zhi-hui-su-shu-xue-407lb/
    def kthCharacter(self, k: int) -> str:
        pos = k
        count = 0  # 记录被 shift 的次数

        # 找出原始 'a' 的第几个字符被变换后的值
        while pos > 1:
            power = 1  # 操作次数
            while power * 2 < pos:
                power *= 2

            # 如果落在右边（shift 部分）
            if pos > power:
                pos -= power
                count += 1
            else:
                # 落在左边（原始部分），只需继续往下查
                continue

        # 最终原始字符是 'a'，它被 shift 了 count 次
        return chr(count % 26 + ord('a'))

class Solution:
    def kthCharacter(self, k: int) -> str:
        return chr(ord('a') + (k - 1).bit_count())
