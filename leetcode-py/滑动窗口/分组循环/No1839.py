class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        n = len(word)
        _set = set("aeiou")
        _map = {'a': 0,
                'e': 1,
                'i': 2,
                'o': 3,
                'u': 4}
        ans = i = 0
        while i < n:
            if word[i] != 'a':
                i += 1
                continue
            start = i
            i += 1
            while i < n and word[i] in _set and (word[i] == word[i - 1] or _map[word[i]] == _map[word[i - 1]] + 1):
                i += 1
            if word[i - 1] == "u":
                ans = max(ans, i - start)
        return ans

            





