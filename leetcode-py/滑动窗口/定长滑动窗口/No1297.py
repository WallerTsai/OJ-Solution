from collections import defaultdict
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        length = len(s)
        adict = defaultdict(int)
        temp_s = ""
        # count = 0
        for i,string in enumerate(s):

            temp_s += string

            if len(temp_s) < minSize:
                continue

            if len(temp_s) > maxSize:
                temp_s = temp_s[1:]

            while len(temp_s) >= minSize:
                if len(set(temp_s)) <= maxLetters:
                    adict[temp_s] += 1
                temp_s = temp_s[1:]

        return max(adict.values()) if adict else 0  # 100ms

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:

        adict = defaultdict(int)
        temp_s = ""

        for i in s:

            temp_s += i

            if len(temp_s) < minSize:
                continue

            if len(temp_s) > maxSize:
                temp_s = temp_s[1:]

            while len(temp_s) >= minSize:
                if len(set(temp_s)) <= maxLetters:
                    adict[temp_s] += 1
                temp_s = temp_s[1:]

        return max(adict.values()) if adict else 0  # 95ms
    
class Solution:
    #如果发现了maxSize没有用，因为长的串重复它的子串一定也重复
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        adict = defaultdict(int)
        temp_s = ""

        for i in s:

            temp_s += i

            if len(temp_s) < minSize:
                continue

            while len(temp_s) >= minSize:
                if len(set(temp_s)) <= maxLetters:
                    adict[temp_s] += 1
                temp_s = temp_s[1:]

        return max(adict.values()) if adict else 0  # 87ms