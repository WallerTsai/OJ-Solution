from collections import Counter


class Solution:
    # counter覆盖
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt1 = Counter(s1)
        length = len(s1)
        cnt2 = Counter()

        left = 0
        for right,c in enumerate(s2):
            if right - left + 1 < length:
                cnt2[c] += 1
                continue

            cnt2[c] += 1
            if cnt1 == cnt2:
                return True
            
            cnt2[s2[left]] -= 1
            if cnt2[s2[left]] == 0:
                cnt2.pop(s2[left])
            left += 1
        return False

fun = Solution()
print(fun.checkInclusion("ab","eidbaooo"))
                



