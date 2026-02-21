import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        hq = []
        for i, ch in enumerate(s):
            if ch == '*':
                _, j = heapq.heappop(hq)
                s[-j] = '*'
            else:
                heapq.heappush(hq, (ch,-i))
        ans = []
        for ch in s:
            if ch != '*':
                ans.append(ch)
        return "".join(ans) # 679ms

class Solution:
    def clearStars(self, s: str) -> str:
        s = list(s)
        stacks = [[] for _ in range(26)]
        for i, c in enumerate(s):
            if c != '*':
                stacks[ord(c) - ord('a')].append(i)
                continue
            for st in stacks:
                if st:
                    s[st.pop()] = '*'
                    break
        return ''.join(c for c in s if c != '*')    # 383ms

fun = Solution()
fun.clearStars("aaba*")