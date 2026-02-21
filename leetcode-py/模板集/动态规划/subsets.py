# subsets
state = 0b1111
subsets = []
s = state
while s:
    subsets.append(s)
    s = (s - 1) & state
subsets.append(0)  # 空集


# submasks
N = 12  # 根据题目修改范围
subsets = [[] for _ in range(1 << N)]
for i in range(1 << N):
    s = i
    while s:
        subsets[i].append(s)
        s = (s - 1) & i