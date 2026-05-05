from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # F(k)=F(k−1)+sum(nums)−len(nums)∗A[len(nums)−k]
        n = len(nums)
        total = sum(nums)
        ans = cur = sum(i * x for i, x in enumerate(nums))
        for i in range(1, n):
            cur = cur + total - n * nums[n - i]
            ans = max(cur, ans)
        return ans


import numpy as np

class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 构造序列 W: [0, 1, 2, ..., n-1]
        W = np.arange(n)
        
        # 构造序列 B: B[i] = nums[-i mod n]
        B = np.zeros(n)
        B[0] = nums[0]
        if n > 1:
            B[1:] = nums[:0:-1] # 除了第0个元素，后面的元素反转
            
        # 计算 W 和 B 的快速傅里叶变换（转入频域）
        fft_W = np.fft.fft(W)
        fft_B = np.fft.fft(B)
        
        # 频域下进行逐元素相乘
        fft_F = fft_W * fft_B
        
        # 逆傅里叶变换（转回时域）
        F = np.fft.ifft(fft_F).real
        
        # 因为 FFT 涉及浮点数(复数)运算，需要用 round 消除精度误差，转回整数
        F = np.round(F).astype(int)
        
        return int(np.max(F))

