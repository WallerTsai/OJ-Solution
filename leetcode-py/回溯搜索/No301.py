from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        valid_right = 0
        cnt = 0
        for ch in s:
            if ch == "(":
                cnt += 1
            elif ch == ")":
                cnt -= 1
                if cnt >= 0:
                    valid_right += 1
                else:
                    cnt = 0
        valid_num = valid_right

        res = set()
        path = []
        def dfs(i: int, cnt: int, cnt_left: int, cnt_right: int):
            if cnt < 0:
                return 
            
            if n - i + 1 < 2 * valid_num - cnt_left - cnt_right:
                return 

            if i == n:
                if cnt == 0 and cnt_left == cnt_right == valid_right:
                    res.add("".join(path))
                return

            # 非括号，不允许不选
            if s[i] not in ("(", ")"):
                path.append(s[i])
                dfs(i + 1, cnt, cnt_left, cnt_right)
                path.pop()
                return    

            nx_cnt = cnt
            nx_cl = cnt_left
            nx_cr = cnt_right
            if s[i] == "(":
                nx_cnt += 1
                nx_cl += 1
            elif s[i] == ")":
                nx_cnt -= 1
                nx_cr += 1

            # 选
            path.append(s[i])
            dfs(i + 1, nx_cnt, nx_cl, nx_cr)
            # 不选
            path.pop()
            dfs(i + 1, cnt, cnt_left, cnt_right)     
            return   
    
        dfs(0, 0, 0, 0)
        return list(res)    # 2872ms


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)

        valid_right = 0
        cnt = 0
        for ch in s:
            if ch == "(":
                cnt += 1
            elif ch == ")":
                cnt -= 1
                if cnt >= 0:
                    valid_right += 1
                else:
                    cnt = 0
        valid_num = valid_right

        res = set()
        path = []
        def dfs(i: int, cnt: int, cnt_left: int, cnt_right: int):
            if cnt < 0:
                return 
            
            if n - i + 1 < 2 * valid_num - cnt_left - cnt_right:
                return 

            if i == n:
                if cnt == 0 and cnt_left == cnt_right == valid_right:
                    res.add("".join(path))
                return

            if s[i] == "(":
                if cnt_left < valid_num:
                    path.append(s[i])
                    dfs(i + 1, cnt + 1, cnt_left + 1, cnt_right)
                    path.pop()
            elif s[i] == ")":
                if cnt_right < valid_num:
                    path.append(s[i])
                    dfs(i + 1, cnt - 1, cnt_left, cnt_right + 1)
                    path.pop()
            else:
                # 非括号，不允许不选
                path.append(s[i])
                dfs(i + 1, cnt, cnt_left, cnt_right)
                path.pop()
                return   
            
            dfs(i + 1, cnt, cnt_left, cnt_right)   

    
        dfs(0, 0, 0, 0)
        return list(res)    # 75ms


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        left_remove, right_remove = 0, 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()
        path = []
        
        def dfs(i, l, r, cnt):
            if i >= n:
                if cnt == 0:
                    ans.add(''.join(path))
                return

            if s[i] == '(':
                if l > 0:
                    dfs(i + 1, l - 1, r, cnt)
                path.append(s[i])
                dfs(i + 1, l, r, cnt + 1)
                path.pop()

            elif s[i] == ')':
                if r > 0:
                    dfs(i + 1, l, r - 1, cnt)
                if cnt > 0 :
                    path.append(s[i])
                    dfs(i + 1, l, r, cnt - 1)
                    path.pop()

            else:
                path.append(s[i])
                dfs(i + 1, l, r, cnt)
                path.pop()

        dfs(0, left_remove, right_remove, 0)
        return list(ans)    # 1347ms


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        n = len(s)
        left_remove, right_remove = 0, 0
        for ch in s:
            if ch == '(':
                left_remove += 1
            elif ch == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1

        ans = set()
        path = []
        
        def dfs(i, l, r, cnt):
            if cnt < 0:
                return 
            
            if n - i + 1 < l + r:
                return

            if i >= n:
                if cnt == 0:
                    ans.add(''.join(path))
                return

            if s[i] == '(':
                if l > 0:
                    dfs(i + 1, l - 1, r, cnt)
                path.append(s[i])
                dfs(i + 1, l, r, cnt + 1)
                path.pop()

            elif s[i] == ')':
                if r > 0:
                    dfs(i + 1, l, r - 1, cnt)
                if cnt > 0 :
                    path.append(s[i])
                    dfs(i + 1, l, r, cnt - 1)
                    path.pop()

            else:
                path.append(s[i])
                dfs(i + 1, l, r, cnt)
                path.pop()

        dfs(0, left_remove, right_remove, 0)
        return list(ans)    # 304ms

