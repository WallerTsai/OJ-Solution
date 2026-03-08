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
st = []
for i in range(len(s)):
    ch = s[i]
    if ch == ')':
        li = []
        while st[-1] != '(':
            li.append(st.pop())
        st.pop()
        out(''.join(reversed(li)))
        print()
        continue
    st.append(ch)


