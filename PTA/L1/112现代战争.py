import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write 


def main():
    n, m, t = mii()
    sorted_li = []
    sq = []
    for i in range(n):
        li = lii()
        for j, x in enumerate(li):
            sorted_li.append((x, i, j))
        sq.append(li)
    row_set = set()
    col_set = set()
    sorted_li.sort(reverse=True)
    for x, i, j in sorted_li:
        if i in row_set or j in col_set:
            continue
        row_set.add(i)
        col_set.add(j)
        t -= 1
        if t == 0:
            break
    
    # 输出
    for i in range(n):
        if i in row_set:
            continue
        li = []
        for j in range(m):
            if j in col_set:
                continue
            li.append(sq[i][j])
        print(*li)

if __name__ == "__main__":
    main()


# gemini AC 代码
import sys

def main():
    # 1. 一次性读取所有数据，避开多次调用的开销
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # 将整个矩阵存入一维列表（列表推导式底层有优化，速度极快）
    vals = [int(x) for x in data[3:]]
    
    # 2. 核心黑科技：直接对 0 到 n*m-1 的下标进行排序
    # key=vals.__getitem__ 相当于告诉 Python 直接去底层拿数据比大小，没有多余的函数调用
    idx_list = sorted(range(n * m), key=vals.__getitem__, reverse=True)
    
    # 3. 使用 bytearray 替代 set (用空间换时间，O(1) 绝对寻址，没有哈希计算)
    row_del = bytearray(n)
    col_del = bytearray(m)
    
    for idx in idx_list:
        # 通过一维坐标还原二维行列号
        r = idx // m
        c = idx % m
        
        # 如果已经被删过了，直接跳过
        if row_del[r] or col_del[c]:
            continue
            
        # 标记删除
        row_del[r] = 1
        col_del[c] = 1
        k -= 1
        if k == 0:
            break
            
    # 4. 极速输出：尽量用列表推导式和 join
    out = []
    for r in range(n):
        if row_del[r]:
            continue
        
        base = r * m
        # 列表推导式过滤被删掉的列，并直接转成字符串
        row_out = [str(vals[base + c]) for c in range(m) if not col_del[c]]
        out.append(" ".join(row_out))
        
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()