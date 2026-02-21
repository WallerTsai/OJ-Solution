
base10 = lambda x: pow(10, x)
class Solution:
    def numberToWords(self, num: int) -> str:
        ones = ("", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen")
        tens = ("", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety")
        large_numbers = ("", "Thousand", "Million", "Billion")
        
        if num == 0:
            return "Zero"
        
        res = []
        for i in range(len(large_numbers) - 1, -1, -1):
            x = num // base10(i * 3) % 1000
            
            if x == 0:
                continue

            if x >= 100:
                res.append(ones[x // 100])
                res.append("Hundred")
            
            if 0 < x % 100 < 20:
                res.append(ones[x % 100])
            elif x % 100 >= 20:
                res.append(tens[x // 10 % 10])
                if x % 10:
                    res.append(ones[x % 10])

            if i:
                res.append(large_numbers[i])

        return " ".join(res)