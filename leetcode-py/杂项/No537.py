class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a1, b1 = map(int, num1[:-1].split('+'))
        a2, b2 = map(int, num2[:-1].split('+'))

        a3 = a1 * a2 - b1 * b2
        b3 = a1 * b2 + a2 * b1
        return f"{a3}+{b3}i"

