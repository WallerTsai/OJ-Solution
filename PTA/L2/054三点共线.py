import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())


out = sys.stdout.write 

n = ii()
data = sys.stdin.read().strip().split()
it = iter(data)

p0_set = set()
p1_set = set()
p2_set = set()
for _ in range(n):
    x, y = int(next(it)), int(next(it))
    if y == 0:
        p0_set.add(x)
    elif y == 1:
        p1_set.add(x)
    else:
        p2_set.add(x)

p0 = sorted(p0_set)
p1 = sorted(p1_set)
ans = []
for x1 in p1:
    for x0 in p0:
        x2 = 2 * x1 - x0
        if x2 in p2_set:
            ans.append(f"[{x0}, 0] [{x1}, 1] [{x2}, 2]")

if ans:
    out("\n".join(ans))
else:
    out("-1")

# 超时


# Gemini代码
# 超时
import sys

def main():
    # 1. 极速读入
    data = sys.stdin.read().split()
    if not data:
        return
        
    n = int(data[0])
    
    # 2. 使用位移和 bytearray 替代 set 查找
    # x 的极值是 1e6，算出来的 x2 极值是 3e6，所以 OFFSET=3000000 绝对安全
    OFFSET = 3000000
    vis = bytearray(6000005)
    
    p0_set = set()
    p1_set = set()
    
    it = iter(data[1:])
    for _ in range(n):
        x, y = int(next(it)), int(next(it))
        if y == 0:
            p0_set.add(x)
        elif y == 1:
            p1_set.add(x)
        elif y == 2:
            vis[x + OFFSET] = 1  # O(1) 物理内存标记
            
    p0 = sorted(p0_set)
    p1 = sorted(p1_set)
    
    ans = []
    # 将方法提取为局部变量，每次调用能省去底层属性查找的时间
    ans_extend = ans.extend 
    
    # 3. 双重循环的极致优化
    for x1 in p1:
        # 将数学计算提到外层，减少内层循环的计算量
        t = 2 * x1
        base = t + OFFSET 
        
        # 核心黑科技：列表推导式
        # 这里的 for 和 if 全部在 C 语言层面运行，避开了 Python 虚拟机的字节码解析
        ans_extend([
            f"[{x0}, 0] [{x1}, 1] [{t - x0}, 2]" 
            for x0 in p0 if vis[base - x0]
        ])

    # 4. 极速输出
    if ans:
        sys.stdout.write("\n".join(ans) + "\n")
    else:
        sys.stdout.write("-1\n")

if __name__ == "__main__":
    main()