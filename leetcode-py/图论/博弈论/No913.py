from collections import deque
from typing import List
MOUSE_TURN = 0
CAT_TURN = 1

DRAW = 0
MOUSE_WIN = 1
CAT_WIN = 2

class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        n = len(graph)

        degrees = [[[0, 0] for _ in range(n)] for _ in range(n)]
        # i 表示 MOUSE 所在节点 ，j 表示 CAT 所在节点
        for i in range(n):
            for j in range(1,n):
                # 记录度数
                degrees[i][j][MOUSE_TURN] = len(graph[i])
                degrees[i][j][CAT_TURN] = len(graph[j])
        for y in graph[0]:
            for i in range(n):
                degrees[i][y][CAT_TURN] -= 1 # 猫无法进洞

        results = [[[0, 0] for _ in range(n)] for _ in range(n)]
        q = deque() # 使用队列枚举情况
        for j in range(1,n): # MOUSE WIN
            results[0][j][MOUSE_TURN] = MOUSE_WIN
            results[0][j][CAT_TURN] = MOUSE_WIN
            q.append((0, j, MOUSE_TURN))
            q.append((0, j, CAT_TURN))
        for i in range(1, n): # CAT WIN
            results[i][i][MOUSE_TURN] = CAT_WIN
            results[i][i][CAT_TURN] = CAT_WIN
            q.append((i, i, MOUSE_TURN))
            q.append((i, i, CAT_TURN))
 
        while q:
            mouse,cat,turn = q.popleft()
            result = results[mouse][cat][turn]

            if turn == MOUSE_TURN:
                prevStates = [(mouse,prev,CAT_TURN) for prev in graph[cat]] # CAT 可能出现的节点
            else:
                prevStates = [(prev, cat, MOUSE_TURN) for prev in graph[mouse]] # MOUSE 可能出现的节点

            for prevMouse,prevCat,prevTurn in prevStates:
                if prevCat == 0:
                    continue # CAT 不能出现在 0 点
                if results[prevMouse][prevCat][prevTurn] == DRAW: # 前置节点为平局
                    # 结果为一方获胜
                    canWin = result == MOUSE_WIN and prevTurn == MOUSE_TURN or result == CAT_WIN and prevTurn == CAT_TURN
                    if canWin:
                        results[prevMouse][prevCat][prevTurn] = result
                        q.append((prevMouse,prevCat,prevTurn)) # 添加至队列
                    else:
                        degrees[prevMouse][prevCat][prevTurn] -= 1
                        if degrees[prevMouse][prevCat][prevTurn] == 0:
                            results[prevMouse][prevCat][prevTurn] = CAT_WIN if prevTurn == MOUSE_TURN else MOUSE_WIN
                            q.append((prevMouse,prevCat,prevTurn))
        
        return results[1][2][MOUSE_TURN]

