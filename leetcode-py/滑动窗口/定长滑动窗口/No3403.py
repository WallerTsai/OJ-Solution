class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word) - numFriends + 1
        ans = max_d = count = left = 0
        
        for right, s in enumerate(word):
            count += ord(s)
            if right - left + 1< n:
                continue
            if count > max_d:
                max_d = count
                ans = left
            count -= ord(word[left])
            left += 1
        
        return word[ans:ans + n]    # 错误， 对题目理解有问题
    
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word
        
        def compare(word1: str, word2: str) -> bool:
            n, m = len(word1), len(word2)
            for i in range(min(n, m)):
                if word1[i] < word2[i]:
                    return True
                elif word1[i] > word2[i]:
                    return False
            return len(word2) > len(word1)


        n = len(word)
        m = n - numFriends + 1
        max_c = 'a'
        index_list = []
        for i, ch in enumerate(word):
            if ch > max_c:
                index_list = [i]
                max_c = ch
            elif ch == max_c:
                index_list.append(i)

        first = index_list[0]
        ans = word[first : min(first + m, n)]
        
        
        for i in index_list[1:]:
            temp = word[i : min(i + m, n)]
            if compare(ans,temp):
                ans = temp

        return ans  # 943ms
    
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word
        
        def compare(word1: str, word2: str) -> bool:
            n, m = len(word1), len(word2)
            for i in range(min(n, m)):
                if word1[i] < word2[i]:
                    return True
                elif word1[i] > word2[i]:
                    return False
            return len(word2) > len(word1)


        n = len(word)
        m = n - numFriends + 1
        ans = word[:min(n,m)]
        for i, ch in enumerate(word):
            if ch > ans[0]:
                ans = word[i:min(n,i+m)]
            elif ch == ans[0]:
                if compare(ans,word[i:min(n,i+m)]):
                    ans = word[i:min(n,i+m)]
            
        return ans  # 1833ms

class Solution:
    def answerString(self, s: str, k: int) -> str:
        if k == 1:
            return s
        n = len(s)
        return max(s[i: i + n - k + 1] for i in range(n))   # 12ms  # 这是最容易想到的，没想到这么快
    
class Solution:
    # 灵神
    # 参考 No1163
    def answerString(self, s: str, numFriends: int) -> str:
        if numFriends == 1:
            return s
        n = len(s)
        i, j = 0, 1
        while j < n:
            k = 0
            while j + k < n and s[i + k] == s[j + k]:
                k += 1
            if j + k < n and s[i + k] < s[j + k]:
                i, j = j, max(j + 1, i + k + 1)
            else:
                j += k + 1
        return s[i: i + n - numFriends + 1] # 11ms
    
