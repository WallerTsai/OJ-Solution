pow_two_sorted_str_set = {''.join(sorted(str(1 << i))) for i in range(30)}

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        s = ''.join(sorted(str(n)))
        return s in pow_two_sorted_str_set