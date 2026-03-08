from collections import Counter
import sys
# sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write 

s = input()
li = lii()

cnt = Counter(s)
ans = sum(li[ord(ch) - ord('a')] * val for ch , val in cnt.items())
ans_li = [cnt[chr(i)] for i in range(ord('a'), ord('a') + 26)]
out(' '.join(map(str, ans_li)))
print()
out(str(ans))




