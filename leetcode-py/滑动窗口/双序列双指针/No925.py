from itertools import groupby

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        i = j = 0 
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif  j >= 1 and typed[j] == typed[j-1]:
                    j += 1
            else:
                return False
        return i == len(name)

    # 需要扫描完typed, 如果后面有多余字符则False


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        def group_counts(s):
            # 使用 groupby 统计每个字符的连续出现次数
            return [(char, len(list(group))) for char, group in groupby(s)]
        
        name_groups = group_counts(name)
        typed_groups = group_counts(typed)
        
        if len(name_groups) != len(typed_groups):
            return False
        
        for (name_char, name_count), (typed_char, typed_count) in zip(name_groups, typed_groups):
            # 检查字符是否一致，以及 typed 中的字符数量是否不少于 name 中的字符数量
            if name_char != typed_char or typed_count < name_count:
                return False
        
        return True
