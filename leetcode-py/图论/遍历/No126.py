from collections import defaultdict, deque
from typing import List
from string import ascii_lowercase

# bfs, dfs 综合运用

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        begin_set = {beginWord}
        p = defaultdict(list)
        word_set.discard(beginWord)
        m = len(beginWord)

        found = False
        while begin_set and not found:
            nx_dict = defaultdict(list)

            for word in begin_set:
                for i in range(m):
                    for ch in ascii_lowercase:
                        if ch == word[i]:
                            continue
                        nx_word = word[:i] + ch + word[i + 1:]
                        if nx_word in word_set:
                            nx_dict[nx_word].append(word)
                            if nx_word == endWord:
                                found = True

            begin_set = set(nx_dict.keys())
            word_set -= begin_set

            for child, parent in nx_dict.items():
                p[child].extend(parent)


        if not found:
            return []
        
        # dfs 回溯路径
        res = []
        path = [endWord]
        def dfs(node):
            if node == beginWord:
                res.append(path[::-1])
                return
            
            for parent in p[node]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return res  # 31ms
    
    

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []

        begin_set = {beginWord}
        p = defaultdict(list)
        word_set.discard(beginWord)
        m = len(beginWord)

        found = False
        while begin_set and not found:
            nx_set = set()
            for word in begin_set:
                for i in range(m):
                    for ch in ascii_lowercase:
                        if ch == word[i]:
                            continue
                        nx_word = word[:i] + ch + word[i + 1:]
                        if nx_word in word_set:
                            nx_set.add(nx_word)
                            p[nx_word].append(word)
                            if nx_word == endWord:
                                found = True

            word_set -= nx_set
            begin_set = nx_set


        if not found:
            return []
        
        # dfs 回溯路径
        res = []
        path = [endWord]
        def dfs(node):
            if node == beginWord:
                res.append(path[::-1])
                return
            
            for parent in p[node]:
                path.append(parent)
                dfs(parent)
                path.pop()

        dfs(endWord)

        return res  # 31ms
    



class Solution:
    # leetcode 最快
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []

        # [与原版相同] 预处理通配符字典
        # 将 "hot" 存为 "*ot", "h*t", "ho*" 对应的列表
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                nei[pattern].append(word)

        # [与原版相同] 队列依然只存储单词本身（为了节省内存，防止 MLE）
        q = deque([beginWord])
        visit = set([beginWord])
        
        # [修改 1] 用于路径重建的数据结构：记录每个节点的父节点列表
        parents = defaultdict(list)
        found = False

        while q and not found:
            # [修改 2] 按“层级”跟踪访问，而不是按“节点”实时跟踪
            # 使用一个临时集合来记录“当前层”访问过的单词。
            # 我们不能在循环内部立即更新全局 'visit' 集合，
            # 因为在单词接龙 II 中，多条路径可能会在同一层到达同一个单词
            # (例如 A->C 和 B->C)，这两条都是有效的最短路径，都需要被记录。
            visited_this_level = set()
            
            for i in range(len(q)):
                word = q.popleft()
                
                # 注意：即使找到了目标，我们也不会立即返回。
                # 必须跑完当前层，以找出连接到 endWord 的 *所有* 父节点。
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neiword in nei[pattern]:
                
                        if neiword not in visit:
                            # [修改 3] 每层仅将单词加入队列一次...
                            # 避免重复入队 (这就是 visited_this_level 的作用)
                            if neiword not in visited_this_level:
                                visited_this_level.add(neiword)
                                q.append(neiword)
                            
                            # [修改 4] ...但每次都要记录父节点关系
                            # 即使该单词已经被当前层的其他父节点访问过，我们依然要记录新的父子关系。
                            parents[neiword].append(word)
                            
                            if neiword == endWord:
                                found = True
            
            # [修改 5] 当前层遍历结束后，才更新全局访问集合
            # 这保证了下一层不会再走回本层已访问过的节点
            visit.update(visited_this_level)

        # [修改 6] 回溯 (DFS) 以重建所有最短路径
        res = []
        def backtrack(node, path):
            if node == beginWord:
                res.append(path)
                return
            for parent in parents[node]:
                backtrack(parent, [parent] + path)

        if found:
            backtrack(endWord, [endWord])
        
        return res  # 7ms

'''
这是针对 LeetCode 126 (Word Ladder II) 的修改版代码。

主要区别在于：Word Ladder I 只要求最短路径的长度，而 Word Ladder II 要求输出所有实际的最短路径。

代码修改点：
逻辑从标准的 BFS 变更为“分层 BFS” (Layered BFS)，我们通过延迟标记访问状态来收集同一层的所有有效路径，并使用父节点映射表来还原路径。

变更总结：

1. 队列内容 (q):
   旧版: 存储单个字符串 (word)。
   新版: 依然存储单个字符串 (word)。*注意：为了节省内存，我们不直接在队列里存路径列表，而是存节点关系。*

2. 访问逻辑 (visit vs visited_this_level):
   旧版: 见到单词立即标记为 visit。这会阻止同一层的其他节点再次访问它。
   新版: 当前层发现的单词先存入 visited_this_level。只有当当前层循环完全结束后，才将其加入全局 visit 集合。这允许了“路径汇聚” (例如 hot 和 dot 都能变成 lot，我们能同时捕捉到 hot->lot 和 dot->lot 这两条有效路径)。

3. 结果处理:
   旧版: 找到 endWord 立即返回步数 (整数)。
   新版: 找到 endWord 后标记 found=True，但在跑完当前层之前不停止。最后利用 parents 字典通过回溯 (Backtracking) 构建完整路径列表。
'''