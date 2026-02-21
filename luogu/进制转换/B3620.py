def x_to_decimal(x: int, S: str) -> int:
    ans = 0
    power = 1
    for c in reversed(S):
        if c.isdigit():
            i = int(c)
        else:
            i = ord(c) - ord('A') + 10
        ans += i * power
        power *= x
    return ans

if __name__ == "__main__":
    x = int(input())
    S = input()
    print(x_to_decimal(x,S))