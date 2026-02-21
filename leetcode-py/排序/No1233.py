from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = [folder[0]]
        for f in folder[1:]:
            last = res[-1]
            if not f.startswith(last + '/'):
                res.append(f)
        return res  # 27ms
    
import re
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = [folder[0]]
        pattern = re.compile(re.escape(folder[0]) + r'/.*')
        for f in folder[1:]:
            if not pattern.match(f):
                result.append(f)
                pattern = re.compile(re.escape(f) + r'/.*')
        return result   # 387ms