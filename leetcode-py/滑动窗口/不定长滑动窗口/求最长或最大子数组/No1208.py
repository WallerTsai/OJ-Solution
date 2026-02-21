class Solution:
    # 不定长滑动窗口 + 双指针 + 哈希
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        costs = [0] * length
        res = left = 0
        for right in range(length):
            cost = abs(ord(s[right]) - ord(t[right]))
            costs[right] = cost
            maxCost -= cost

            while maxCost < 0:
                maxCost += costs[left]
                left += 1

            res = max(res,right-left+1)

        return res  # 27ms


class Solution:
    # 只增大的伪定长滑动窗口 + 双指针 + 哈希
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        length = len(s)
        costs = [0] * length
        left = 0
        for right in range(length):
            cost = abs(ord(s[right]) - ord(t[right]))
            costs[right] = cost
            maxCost -= cost

            if maxCost < 0:
                maxCost += costs[left]
                left += 1

        return right-left+1 # 11ms 全站最快