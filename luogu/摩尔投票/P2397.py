from collections import defaultdict
from typing import List
import sys
sys.setrecursionlimit(1_000_000_000)

input = lambda: sys.stdin.readline().rstrip()
ii = lambda: int(input())
mii = lambda: map(int, input().split())
lii = lambda: list(mii())

# data = sys.stdin.read().strip().split()
# it = iter(data)

out = sys.stdout.write     

def majorityElement_k(nums: List[int], k: int) -> list[int]:
    n = len(nums)
    if n == 0 or k < 2:
        return []

    candidates = {} 
    for num in nums:
        if num in candidates:
            candidates[num] += 1
        elif len(candidates) < k - 1:
            candidates[num] = 1
        else:
            for key in list(candidates.keys()):
                candidates[key] -= 1
                if candidates[key] == 0:
                    del candidates[key]

    result = set()
    counts = defaultdict(int)
    for num in nums:
        if num in candidates:
            counts[num] += 1
            if counts[num] > n // k:
                result.add(num)

    return list(result)

    
def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = next(it)
    ans = hp = 0
    for x in next(it):
        if hp == 0:
            ans, hp = x, 1
        else:
            hp += 1 if x == ans else - 1

    out(str(ans))

if __name__ == "__main__":
    main()