# 设总共跳了 x 次数，最远距离 S 为 x * (x + 1) // 2
# 再假设中途向反方向跳的总距离和为 K
# 则： L = S - 2K
# 条件：
# 距离够远：最大的跳跃总和 S 必须大于等于目标距离 L。即 S >= L。
# 奇偶性相同：因为 S - L = 2K（2K 必然是个偶数），所以 S 和 L 的奇偶性必须完全一样。
# 只要奇偶性一样，且 S >= L，我们总是能从 1 到 x 中凑出一个和为 K 的组合（这是数学上可以证明的性质）。


from itertools import count


def main():
    L = int(input())
    left, right = 1, 1414213562 + 1

    x = right
    while left <= right:
        mid = (left + right) // 2
        if mid * (mid + 1) // 2 >= L:
            x = mid
            right = mid - 1
        else:
            left = mid + 1
    
    while True:
        S = x * (x + 1) // 2
        if S >= L and (S - L) % 2 == 0:
            print(x)
            return
        x += 1
    
if __name__ == "__main__":
    main()



target = pow(10, 18)
for i in count(1):
    if i * (i + 1) // 2 >= target:
        print(i)
        break






