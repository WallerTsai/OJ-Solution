from collections import defaultdict
from typing import List

# 每个节点最多只有一个出边，不需要建图
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:

        n = len(edges)

        def bfs(node):
            adict = defaultdict(int)
            d = 0
            while node >= 0 and node not in adict:
                adict[node] = d
                d += 1
                node = edges[node]

            return adict

        dict1, dict2 = bfs(node1), bfs(node2)
        print(dict1.items())
        print(dict2.items())

        d = n + 1
        ans = n
        for i, x in dict1.items():
            if i in dict2:
                max_d = max(x, dict2[i])
                if d > max_d:
                    ans = i
                    d = max_d
                elif d == max_d:
                    ans = min(i, ans)

        return ans if ans != n else -1
    
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        def calc_dis(x: int) -> List[int]:
            dis = [n] * n  # 初始化成 n，表示无法到达或者尚未访问的节点
            d = 0
            # 从 x 出发，直到无路可走（x=-1）或者重复访问节点（dis[x]<n）
            while x >= 0 and dis[x] == n:
                dis[x] = d
                d += 1
                x = edges[x]
            return dis

        dis1 = calc_dis(node1)
        dis2 = calc_dis(node2)

        min_dis, ans = n, -1
        for i, (d1, d2) in enumerate(zip(dis1, dis2)):
            d = max(d1, d2)
            if d < min_dis:
                min_dis, ans = d, i
        return ans