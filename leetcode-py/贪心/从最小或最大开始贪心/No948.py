from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        if len(tokens) == 0:
            return 0
        tokens.sort()
        res = 0
        all_sum = sum(tokens)
        left = 0
        right = len(tokens)-1

        while(left < right):

            if power >= all_sum:
                res += right-left+1
                break

            if tokens[left] <= power:
                power -= tokens[left]
                all_sum -= tokens[left]
                res += 1
                left += 1
            else:
                if res != 0:
                    power += tokens[right]
                    all_sum -= tokens[right]
                    res -= 1
                    right -= 1
                else:
                    break
        else:
            if power >= tokens[left]:
                res += 1


        return res  # 2ms


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()  # 对令牌按值排序
        a, b = 0, len(tokens) - 1  # 使用两个指针，a指向最小值，b指向最大值
        score = 0  # 当前分数
        max_score = 0  # 记录最大分数

        while a <= b:
            if power >= tokens[a]:  # 如果有足够的能量来使用 "朝上" 策略
                power -= tokens[a]  # 消耗 tokens[a] 点能量
                score += 1  # 得到 1 分
                a += 1  # 移动指针，使用了一个最小的令牌
            elif score > 0:  # 如果当前有分数，可以使用 "朝下" 策略
                power += tokens[b]  # 增加 tokens[b] 点能量
                score -= 1  # 失去 1 分
                b -= 1  # 移动指针，使用了一个最大的令牌
            else:
                break  # 如果没有足够能量且没有分数，结束循环

            max_score = max(max_score, score)  # 更新最大分数

        return max_score    # 3ms
