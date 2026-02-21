from collections import defaultdict

class Spreadsheet:
    # 139ms
    def __init__(self, rows: int):
        self.rows = rows
        self.maps = defaultdict(list)

    def setCell(self, cell: str, value: int) -> None:
        line, row = cell[0], int(cell[1:]) - 1
        if not self.maps[line]:
            self.maps[line] = [0] * self.rows
        self.maps[line][row] = value

    def resetCell(self, cell: str) -> None:
        line, row = cell[0], int(cell[1:]) - 1
        if self.maps[line]:
            self.maps[line][row] = 0

    def getValue(self, formula: str) -> int:
        ans = 0
        s = formula[1:].split("+")
        for c in s:
            if not c.isdigit():
                if self.maps[c[0]]:
                    ans += self.maps[c[0]][int(c[1:]) - 1]
                else:
                    ans += 0
            else:
                ans += int(c)
        return ans

class Spreadsheet:
    # 灵神 86ms
    def __init__(self, rows: int):
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        self.data.pop(cell, None)

    def getValue(self, formula: str) -> int:
        ans = 0
        for cell in formula[1:].split("+"):
            # 注：如果用 defaultdict(int)，哪怕是访问 self.data[cell] 也会把 cell 插入哈希表，增加空间复杂度
            ans += self.data.get(cell, 0) if cell[0].isupper() else int(cell)
        return ans
    

# 2026年1月12日
class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.data = dict()

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value
        
    def resetCell(self, cell: str) -> None:
        self.data.pop(cell, None)

    def getValue(self, formula: str) -> int:
        res = 0
        for cell in formula[1:].split('+'):
            if cell[0].isupper():
                res += self.data.get(cell, 0)
            else:
                res += int(cell)
        return res

