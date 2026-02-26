from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cnt_languages = defaultdict(set)
        for i, l in enumerate(languages, start=1):
            cnt_languages[i] = set(l)
        
        ans = inf
        for i in range(1, n + 1):
            count = 0
            temp_cnt = {k: set(v) for k, v in cnt_languages.items()}
            for a, b in friendships:
                if temp_cnt[a] & temp_cnt[b]:
                    continue
                if i not in temp_cnt[a]:
                    count += 1
                    temp_cnt[a].add(i)
                if i not in temp_cnt[b]:
                    count += 1
                    temp_cnt[b].add(i)
            ans = min(ans, count)

        return ans  # 超时
    
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cnt_languages = defaultdict(set)
        for i, l in enumerate(languages, start=1):
            cnt_languages[i] = set(l)

        disconnect = []
        for a, b in friendships:
            if not cnt_languages[a] & cnt_languages[b]:
                disconnect.append((a, b))

        ans = inf
        for i in range(1, n + 1):
            count = 0
            temp_cnt = {k: set(v) for k, v in cnt_languages.items()}
            for a, b in disconnect:
                if i not in temp_cnt[a]:
                    count += 1
                    temp_cnt[a].add(i)
                if i not in temp_cnt[b]:
                    count += 1
                    temp_cnt[b].add(i)
            ans = min(ans, count)

        return ans  # 8248ms
    
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cnt_languages = defaultdict(set)
        for i, l in enumerate(languages, start=1):
            cnt_languages[i] = set(l)

        disconnect = []
        for a, b in friendships:
            if not cnt_languages[a] & cnt_languages[b]:
                disconnect.append((a, b))

        # 和灵神相比，上面代码更加费时一点

        ans = inf
        for i in range(1, n + 1):
            temp = set()
            for a, b in disconnect:
                if i not in cnt_languages[a]:
                    temp.add(a)
                if i not in cnt_languages[b]:
                    temp.add(b)
            ans = min(ans, len(temp))

        return ans  # 110ms
    
class Solution:
    # 灵神
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        learned = list(map(set, languages))

        todo_list = []
        for u, v in friendships:
            # u 和 v 减一，下标从 0 开始
            if learned[u - 1].isdisjoint(learned[v - 1]):  # 无交集
                todo_list.append((u - 1, v - 1))

        ans = inf
        for k in range(1, n + 1):  # 枚举需要教的语言 k
            st = set()
            for u, v in todo_list:
                if k not in learned[u]:  # u 需要学习语言 k
                    st.add(u)
                if k not in learned[v]:  # v 需要学习语言 k
                    st.add(v)
            ans = min(ans, len(st))  # len(st) 是需要学习语言 k 的人数
        return ans
    
# 以上暴力可过

class Solution:
    # 另外一种方法
    # 比如有 10 个人无法沟通，其中说中文的人最多，有 8 个，那么只需教剩下的 10−8=2 个人中文（少数服从多数）
    # 灵神
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        learned = list(map(set, languages))

        todo = set()  # 需要学语言的人
        for u, v in friendships:
            # u 和 v 减一，下标从 0 开始
            if learned[u - 1].isdisjoint(learned[v - 1]):  # 无交集
                todo.add(u - 1)
                todo.add(v - 1)

        cnt = [0] * (n + 1)
        for u in todo:
            for x in languages[u]:
                cnt[x] += 1

        return len(todo) - max(cnt)

fun = Solution()
fun.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]])