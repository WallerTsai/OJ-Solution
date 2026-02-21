from math import inf
from typing import List
class Solution:
    # 使用朴素Dijkstra
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #构造邻接矩阵
        AdjMatrix = [[inf for _ in range(n)] for _ in range(n)]
        for u,v,w in times:
            AdjMatrix[u-1][v-1] = w

        # 定义 distance[i] 表示起点 k 到节点 i 的最短路长度
        # inf 表示到不了
        # 正数 表示到这个点的权值
        distance = [inf] * n
        #第k个点设置为0
        res = distance[k-1] = 0

        visited = [False] * n

        while True:
            node = -1
            
            # 找到未访问 且 起点k到另外一个节点权值最小的点
            # 第一趟为起点
            for i,visit in enumerate(visited):
                if not visit and (node < 0 or distance[i] < distance[node]):
                    node = i

            # 全部点都访问过
            if node < 0:
                return res
            
            # 有节点到不了
            if distance[node] == inf:
                return -1

            # 更新res和visited
            res = distance[node]
            visited[node] = True

            # 更新distance
            # 取 当前起点k到别的点的权值 和 起点k吞并node后到别的点的权值 的最小值
            for target_,distance_ in enumerate(AdjMatrix[node]):
                distance[target_] = min(distance[target_],distance[node] + distance_)

fun = Solution()
fun.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]],4,2)