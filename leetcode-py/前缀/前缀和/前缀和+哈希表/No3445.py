from math import inf


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # 将字符串 s 转成数字列表
        s = list(map(int, s))
        ans = -inf

        # 遍历所有数字对 (x, y)
        for x in range(5):
            for y in range(5):
                if y == x:  # 不同字符
                    continue
                
                # win_cnt 记录当前窗口中每个数字的出现次数
                win_cnt = [0] * 5
                # pre_cnt 记录左指针前的数字出现次数
                pre_cnt = [0] * 5
                
                # min_diff 用来存储不同奇偶组合下的最小值，2x2矩阵
                # min_diff[p][q]表示 pre_cnt[x] 奇偶性为 p，pre_s[y] 奇偶性为 q 时的最小差值
                min_diff = [[inf, inf], [inf, inf]]
                
                left = 0  # 左指针
                for i, v in enumerate(s):
                    win_cnt[v] += 1
                    right = i + 1  # 当前右指针
                    
                    # 窗口长度满足且奇偶数值为正，尝试移动左指针缩小窗口
                    while right - left >= k and win_cnt[x] > pre_cnt[x] and win_cnt[y] > pre_cnt[y]:
                        # 计算 pre_cnt[x] 和 pre_cnt[y] 的奇偶性
                        pre_x_parity = pre_cnt[x] & 1  # pre_cnt[x] 的奇偶性，0表示偶数，1表示奇数
                        pre_y_parity = pre_cnt[y] & 1  # pre_cnt[y] 的奇偶性
                        
                        # 更新 min_diff 矩阵中对应奇偶组合的最小值
                        current_diff = pre_cnt[x] - pre_cnt[y]
                        if current_diff < min_diff[pre_x_parity][pre_y_parity]:
                            min_diff[pre_x_parity][pre_y_parity] = current_diff
                        
                        # 左指针对应数字移出窗口，更新 pre_cnt
                        pre_cnt[s[left]] += 1
                        left += 1
                    
                    if right >= k:  # 确保左指针>=0
                        # 计算当前窗口中 x 和 y 的奇偶性
                        cur_x_parity = win_cnt[x] & 1
                        cur_y_parity = win_cnt[y] & 1
                        
                        # 使用 ^1 进行奇偶取反，这样 x 才是奇数，y不变就是偶数
                        min_s_value = min_diff[cur_x_parity ^ 1][cur_y_parity]
                        
                        # 右边界最值-左边界最值
                        candidate = win_cnt[x] - win_cnt[y] - min_s_value
                        if candidate > ans:
                            ans = candidate

        return ans

# 作者：wxyz
